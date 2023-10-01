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

  it(`/GET wallet/quote`, async () => {
    await request(app.getHttpServer())
      .get('/wallet/quote')
      .send({
        fromTokenAddress: '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE',
        toTokenAddress: '0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063',
        walletAddress: '0x4acB15Eb89cC8e396FaFd1117A0c5c414c20b5C2',
        amount: '1000000000000000000',
        mode: 'fixed_from_amount',
      })
      .expect(200)
      .expect((res: request.Response) => {
        expect(res.body.fromamount).toBeDefined();
        expect(res.body.toamount).toBeDefined();
        expect(res.body.estimatedGas).toBeLessThanOrEqual(250000);
      });

    await request(app.getHttpServer())
      .get('/wallet/quote')
      .expect(400)
      .expect((res: request.Response) => {
        expect(res.body.error).toBeDefined();
      });
  });

  it(`/POST wallet/swap`, async () => {
    await request(app.getHttpServer())
      .post('/wallet/swap')
      .send({
        fromTokenAddress: '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE',
        toTokenAddress: '0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063',
        walletAddress: '0x4acB15Eb89cC8e396FaFd1117A0c5c414c20b5C2',
        amount: '1000000000000000000',
        mode: 'fixed_to_amount',
        slippage: 0.1,
        private_key: process.env.PRIVATE_KEY,
      })
      .expect(201)
      .expect((res: request.Response) => {
        expect(res.body).toBeDefined();
      });

    await request(app.getHttpServer())
      .post('/wallet/swap')
      .expect(400)
      .expect((res: request.Response) => {
        expect(res.body.error).toBeDefined();
      });
  }, 60000);

  afterAll(async () => {
    await app.close();
  });
});
