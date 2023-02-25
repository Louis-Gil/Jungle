import { Injectable } from '@nestjs/common';
import axios from 'axios';

@Injectable()
export class WalletService {
  async quote(tokenAddress, walletAddress) {
    const remain = await this.checkCoin(tokenAddress, walletAddress);

    return remain;
  }

  async swap() {
    return 'swap';
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
