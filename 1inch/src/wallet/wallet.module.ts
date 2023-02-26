import { Module } from '@nestjs/common';
import { Web3Service } from 'nest-web3';
import { WalletController } from './wallet.controller';
import { WalletService } from './wallet.service';

@Module({
  controllers: [WalletController],
  providers: [WalletService],
})
export class WalletModule {}
