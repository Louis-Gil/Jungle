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

  async quote(fromTokenAddress, toTokenAddress, walletAddress, amount) {
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

  async swap(fromTokenAddress, toTokenAddress, walletAddress, amount) {
    const result = [];
    const quote = await this.quote(
      fromTokenAddress,
      toTokenAddress,
      walletAddress,
      amount,
    );

    if (fromTokenAddress != '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE') {
      const approve = await this.approve(
        fromTokenAddress,
        walletAddress,
        amount,
      );
      result.push(approve);
    }

    result.push(quote);
    return quote;
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
    const approve = await this.oneInchApi('/approve/transaction', {
      tokenAddress,
      amount,
    });
    approve.from = walletAddress;
    approve.gas = 1000000;

    // const transaction = await this.web3.eth.sendTransaction(approve);
    return approve;
  }
}
