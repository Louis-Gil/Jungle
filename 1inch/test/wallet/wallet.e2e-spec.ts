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
      .expect(200)
      .expect({
        message: 'Hello World!',
      });
  });

  afterAll(async () => {
    await app.close();
  });
});
