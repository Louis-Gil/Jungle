import { Injectable } from '@nestjs/common';

@Injectable()
export class WalletService {
  async quote() {
    return 'quote';
  }

  async swap() {
    return 'swap';
  }
}
