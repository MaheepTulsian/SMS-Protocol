# SMS Protocol
# SMS-Based Crypto Transactions with Blockchain Integration

This project provides a solution for conducting secure cryptocurrency transactions using **SMS**, aimed at promoting **financial inclusion** in underserved communities. By leveraging **Multi-Party Computation (MPC)** for enhanced security, the platform allows users to perform crypto transactions without the need for smartphones or reliable internet access, making it accessible to a broader audience.

## Features

- **SMS-based cryptocurrency transactions**: Users can send and receive crypto by simply texting a formatted SMS.
- **Enhanced security with MPC**: Private keys are split using **Multi-Party Computation (MPC)** to ensure no single party ever has full access to the private key, significantly reducing the risk of fraud or theft.
- **Supports feature phones**: No need for smartphones or internet connection to perform transactions, making it accessible to those in rural or low-tech areas.
- **User-friendly**: Transactions are initiated via simple SMS messages, making it easy for non-technical users to interact with cryptocurrency.

## Technologies Used

- **Twilio**: SMS API for sending and receiving text messages.
- **Blockchain (Ethereum & Avalanche)**: Decentralized systems for secure, transparent crypto transactions.
- **Multi-Party Computation (MPC)**: Enhanced security for managing private keys.
- **React**: Frontend framework for user interface.
- **Node.js & Express**: Backend services for handling SMS requests and blockchain integration.
- **Web3.js & ethers.js**: JavaScript libraries for interacting with the Ethereum and Avalanche blockchains.

## How It Works

1. **SMS Setup**: Users send a formatted SMS like `SEND 0.5 ETH TO 0x123abc...` to initiate a transaction.
2. **Backend Processing**: The backend processes the incoming SMS, validates the transaction, and extracts necessary details like the amount and recipient address.
3. **Blockchain Integration**: The transaction is verified and submitted to the blockchain (Ethereum, Avalanche) using **Web3.js** or **ethers.js**.
4. **Security with MPC**: Private keys are split using **Multi-Party Computation (MPC)** to ensure that no single entity can access the full key, improving security for users.

![99cf98c1-d758-4c6b-b301-a9be594175e1](https://github.com/user-attachments/assets/0983daeb-5166-40e0-8cc7-1ce0d0c2a211)

![d2c5b1f6-5c2c-42ac-b3af-9d247b61cd12](https://github.com/user-attachments/assets/573d15b1-ebb4-49f4-90ba-eae76963d02c)

![8104bbd6-0090-4a82-b19c-d0ee1054195d](https://github.com/user-attachments/assets/310af6a9-03fd-43d6-824d-256e0162dc62)
