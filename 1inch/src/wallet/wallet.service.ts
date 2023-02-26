import { Injectable } from '@nestjs/common';
import axios from 'axios';
import { Web3Service } from 'nest-web3';

@Injectable()
export class WalletService {
  constructor(private readonly web3Service: Web3Service) {}

  web3 = this.web3Service.getClient('eth');
  wallet = this.web3.eth.accounts.wallet.add(process.env.PRIVATE_KEY);
  chainId = 137;
  apiBaseUrl = 'https://api.1inch.io/v5.0/' + this.chainId;

  async getQuote(fromTokenAddress, toTokenAddress, walletAddress, amount) {
    const result = [];
    const remain = await this.oneInchApi('/approve/allowance', {
      tokenAddress: fromTokenAddress,
      walletAddress,
    });
    const quotes = await this.oneInchApi('/quote', {
      fromTokenAddress,
      toTokenAddress,
      amount,
    });
    result.push(remain);
    result.push(quotes);
    return result;
  }

  async postSwap(
    fromTokenAddress,
    toTokenAddress,
    walletAddress,
    amount,
    slippage,
  ) {
    const result = [];
    const quote = await this.getQuote(
      fromTokenAddress,
      toTokenAddress,
      walletAddress,
      amount,
    );
    result.push(quote);
    console.log('after quote');

    if (fromTokenAddress != '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE') {
      const approve = await this.approve(
        fromTokenAddress,
        walletAddress,
        amount,
      );
      result.push(approve);
    }

    const response = await this.oneInchApi('/swap', {
      fromTokenAddress,
      toTokenAddress,
      amount,
      fromAddress: this.wallet.address,
      slippage,
      disableEstimate: true,
    });

    console.log(response);
    response.tx.gas = 1000000;
    const transaction = await this.web3.eth.sendTransaction(response.tx);

    if (transaction.status) {
      console.log('Transaction success');
    } else {
      console.log('Transaction failed');
    }

    result.push(quote);
    result.push(transaction);
    return result;
  }

  async oneInchApi(methodName, queryParams) {
    try {
      const url =
        this.apiBaseUrl +
        methodName +
        '?' +
        new URLSearchParams(queryParams).toString();
      const { data } = await axios.get(url);
      return data;
    } catch (e) {
      console.log(e);
    }
  }

  async approve(tokenAddress, walletAddress, amount) {
    try {
      const approve = await this.oneInchApi('/approve/transaction', {
        tokenAddress,
        amount,
      });
      console.log(approve);

      approve.gas = 1000000;
      approve.from = this.wallet.address;

      const transaction = await this.web3.eth.sendTransaction(approve);
      console.log(transaction);
      if (transaction.status) {
        console.log('Transaction success');
      } else {
        console.log('Transaction failed');
      }
      return transaction;
    } catch (e) {
      console.log(e);
    }
  }
}
