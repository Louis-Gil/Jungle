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

  async quote(tokenAddress, walletAddress) {
    const result = [];
    const remain = await this.oneInchApi('/approve/allowance', {
      tokenAddress,
      walletAddress,
    });
    if (tokenAddress != '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE') {
      const approve = await this.approve(tokenAddress);
      result.push(approve);
    }

    result.push(remain);
    return result;
  }

  async swap() {
    return 'swap';
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

  async approve(tokenAddress) {
    const approve = await this.oneInchApi('/approve/transaction', {
      tokenAddress,
      amount: `1000000000000000000`,
    });
    approve.from = this.wallet.address;
    approve.gas = 1000000;

    // const transaction = await this.web3.eth.sendTransaction(approve);
    return approve;
  }
}
