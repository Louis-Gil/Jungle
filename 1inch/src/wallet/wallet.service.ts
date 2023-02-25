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
    const remain = await this.oneInchApi('/approve/allowance', {
      tokenAddress,
      walletAddress,
    });
    const approve = await this.oneInchApi('/approve/transaction', {
      tokenAddress,
      amount: `1000000000000000000`,
    });
    approve.from = this.wallet.address;
    approve.gas = 100000;
    
    // const transaction = await this.web3.eth.sendTransaction(approve);

    const result = [];
    result.push(remain);
    result.push(approve);
    // result.push(transaction);
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
}
