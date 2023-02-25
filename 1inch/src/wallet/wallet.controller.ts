import { Controller, Get, Post } from '@nestjs/common';
import { WalletService } from './wallet.service';

@Controller('wallet')
export class WalletController {
  constructor(private readonly walletService: WalletService) {}

  @Get('/quote')
  async quote() {
    return this.walletService.quote();
  }

  @Post('/swap')
  async swap() {
    return this.walletService.swap();
  }
}
