from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

# ==== INIT ====
app = FastAPI()

MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

INFURA_API_KEY = os.getenv("INFURA_API_KEY")
RAW_SENDER_ADDRESS = os.getenv("RAW_SENDER_ADDRESS")
CHAIN_ID = int(os.getenv("CHAIN_ID"))
INFURA_URL = f"https://sepolia.infura.io/v3/{INFURA_API_KEY}"

mongo_client = MongoClient(MONGO_URL)
db = mongo_client[DB_NAME]
wallets = db[COLLECTION_NAME]

w3 = Web3(Web3.HTTPProvider(INFURA_URL))
SENDER_ADDRESS = w3.to_checksum_address(RAW_SENDER_ADDRESS)

# ==== SCHEMAS ====
class WalletRegister(BaseModel):
    phone: str
    wallet_address: str
    private_key_1: str

class TransactionRequest(BaseModel):
    phone: str
    receiver_address: str
    amount: float
    private_key_2: str

# ==== ROUTES ====

@app.post("/register-wallet/")
def register_wallet(data: WalletRegister):
    existing = wallets.find_one({"phone": data.phone})
    if existing:
        raise HTTPException(status_code=400, detail="Phone already registered.")

    wallets.insert_one({
        "phone": data.phone,
        "wallet_address": data.wallet_address,
        "private_key_part1": data.private_key_1
    })

    return {"message": "Wallet registered successfully."}

@app.post("/send-transaction/")
def send_transaction_api(data: TransactionRequest):
    wallet = wallets.find_one({"phone": data.phone})
    print(wallet)
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found.")

    full_private_key = (wallet["private_key_part1"] + data.private_key_2).strip()
    print(full_private_key)

    try:
        sender_address = w3.to_checksum_address(wallet["wallet_address"])
        to_address = w3.to_checksum_address(data.receiver_address)
        value = w3.to_wei(data.amount, 'ether')
        nonce = w3.eth.get_transaction_count(sender_address)
        gas_price = w3.eth.gas_price

        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': value,
            'gas': 21000,
            'gasPrice': gas_price,
            'chainId': CHAIN_ID,
            'from': sender_address
        }

        signed_tx = w3.eth.account.sign_transaction(tx, full_private_key)
        # tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

        tx_hash_hex = w3.to_hex(tx_hash)

        return {
            "message": "Transaction successful.",
            "tx_hash": tx_hash_hex,
            "etherscan": f"https://sepolia.etherscan.io/tx/{tx_hash_hex}"
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Transaction failed: {str(e)}")
    