import {
  Controller,
  Get,
  Post,
  UsePipes,
  ValidationPipe,
} from '@nestjs/common';
import { Body } from '@nestjs/common/decorators';
import { WalletRequestDto } from './dto/wallet.dto';
import { WalletService } from './wallet.service';

@Controller('wallet')
export class WalletController {
  constructor(private readonly walletService: WalletService) {}

  @Get('/quote')
  @UsePipes(new ValidationPipe({ transform: true }))
  async Quote(@Body() walletRequestDto: WalletRequestDto) {
    return this.walletService.getQuote(walletRequestDto);
  }

  @Post('/swap')
  @UsePipes(new ValidationPipe({ transform: true }))
  async Swap(@Body() walletRequestDto: WalletRequestDto) {
    return this.walletService.postSwap(walletRequestDto);
  }
}
