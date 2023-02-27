import { AppModule } from './../../src/app.module';
import * as request from 'supertest';
import { Test } from '@nestjs/testing';
import { WalletModule } from './../../src/wallet/wallet.module';
import { WalletService } from './../../src/wallet/wallet.service';
import { INestApplication } from '@nestjs/common';

describe('Wallet', () => {
  let app: INestApplication;
  let walletService: WalletService;

  beforeAll(async () => {
    const moduleRef = await Test.createTestingModule({
      imports: [AppModule, WalletModule],
    })
      .overrideProvider(WalletService)
      .useValue(walletService)
      .compile();

    app = moduleRef.createNestApplication();
    await app.init();
  });

  it(`/GET wallet/quote`, () => {
    return request(app.getHttpServer())
      .get('/wallet/quote')
      .send({
        fromTokenAddress: '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE',
        toTokenAddress: '0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063',
        walletAddress: '0x4acB15Eb89cC8e396FaFd1117A0c5c414c20b5C2',
        amount: '1000000000000000000',
        mode: 'fixed_to_amount',
      })
      .expect(200);
  });

  afterAll(async () => {
    await app.close();
  });
});
