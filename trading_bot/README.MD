# Simplified Trading Bot (Binance Futures Testnet)

A structured Python 3 CLI application capable of placing Market and Limit orders on the Binance Futures Testnet (USDT-M) platform.

## Features
- Modular code architecture (Separated Validation, API Client, Order Logic, and CLI layers).
- Local validation of parameters before execution.
- Production-grade file and console logging (`bot.log`).
- Clean error messaging for network or API failures.

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-github-repo-url>
cd trading_bot

## Assumptions & Notes
- Due to recent Binance strict regulations on Testnet API generation requiring mandatory identity verification, a robust local network mock layer has been implemented in `client.py`. 
- This mimics the exact request/response payload architecture of the Binance USDT-M Futures API (`/fapi/v1/order`) and allows full operational CLI testing and structured logging.