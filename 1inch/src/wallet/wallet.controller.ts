import { Controller, Get, Post } from '@nestjs/common';
import { WalletService } from './wallet.service';

@Controller('wallet')
export class WalletController {
  constructor(private readonly walletService: WalletService) {}

  @Get('/quote')
  async quote(
    fromTokenAddress: string = process.env.FROMTOKEN_ADDRESS,
    toTokenAddress: string = process.env.TOTOKEN_ADDRESS,
    walletAddress: string = process.env.WALLET_ADDRESS,
    amount: string = process.env.AMOUNT,
  ) {
    return this.walletService.quote(
      fromTokenAddress,
      toTokenAddress,
      walletAddress,
      amount,
    );
  }

  @Post('/swap')
  async swap(
    fromTokenAddress: string = process.env.FROMTOKEN_ADDRESS,
    toTokenAddress: string = process.env.TOTOKEN_ADDRESS,
    walletAddress: string = process.env.WALLET_ADDRESS,
    amount: string = process.env.AMOUNT,
    slippage = 0.1,
  ) {
    return this.walletService.swap(
      fromTokenAddress,
      toTokenAddress,
      walletAddress,
      amount,
      slippage,
    );
  }
}
