import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { Web3Module } from 'nest-web3';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { WalletModule } from './wallet/wallet.module';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    Web3Module.forRoot({
      name: 'eth',
      url: 'https://polygon-mainnet.g.alchemy.com/v2/60rwZcE5wFclpIwf7DjIxVteNUixtMlg',
    }),
    WalletModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
