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
    const remain = await this.checkCoin(tokenAddress, walletAddress);
    return remain;
  }

  async swap() {
    return 'swap';
  }

  async apiRequestUrl(methodName, queryParams) {
    return (
      this.apiBaseUrl +
      methodName +
      '?' +
      new URLSearchParams(queryParams).toString()
    );
  }

  async checkCoin(tokenAddress, walletAddress) {
    try {
      const url = await this.apiRequestUrl('/approve/allowance', {
        tokenAddress,
        walletAddress,
      });
      const { data } = await axios.get(url);
      return data;
    } catch (e) {
      console.log(e);
    }
  }
}
