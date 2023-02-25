import { Injectable } from '@nestjs/common';
import axios from 'axios';
import Web3 from 'web3';

@Injectable()
export class WalletService {
  web3RpcUrl = 'https://rpc-mainnet.matic.network';
  web3 = new Web3(this.web3RpcUrl);

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
    return this.apiBaseUrl + methodName
      ? new URLSearchParams(queryParams).toString()
      : '';
  }

  async checkCoin(tokenAddress, walletAddress) {
    try {
      const { data } = await axios.get(
        `https://api.1inch.io/v5.0/137/approve/allowance?tokenAddress=${tokenAddress}&walletAddress=${walletAddress}`,
      );
      return data;
    } catch (e) {
      console.log(e);
    }
  }
}
