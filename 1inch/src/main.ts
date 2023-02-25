import * as dotenv from 'dotenv';
dotenv.config();
import { SuccessInterceptor } from './common/interceptors/success.interceptor';
import { LoggingInterceptor } from './common/interceptors/logging.interceptor';
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalInterceptors(new LoggingInterceptor(), new SuccessInterceptor());
  await app.listen(3000);
}
bootstrap();
