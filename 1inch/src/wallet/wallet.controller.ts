import { Controller, Get, Post } from '@nestjs/common';
import { WalletService } from './wallet.service';

@Controller('wallet')
export class WalletController {
  constructor(private readonly walletService: WalletService) {}

  @Get('/quote')
  async quote(
    tokenAddress: string = process.env.TOKEN_ADDRESS,
    walletAddress: string = process.env.WALLET_ADDRESS,
  ) {
    return this.walletService.quote(tokenAddress, walletAddress);
  }

  @Post('/swap')
  async swap() {
    return this.walletService.swap();
  }
}
