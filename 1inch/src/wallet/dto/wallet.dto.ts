import { IsString, IsNumber, IsNotEmpty } from 'class-validator';

export class WalletRequestDto {
  @IsNotEmpty()
  @IsString()
  fromTokenAddress: string;

  @IsNotEmpty()
  @IsString()
  toTokenAddress: string;

  @IsNotEmpty()
  @IsString()
  walletAddress: string;

  @IsNotEmpty()
  @IsString()
  amount: string;

  @IsNotEmpty()
  @IsString()
  mode: string;

  slippage?: number;
  private_key?: string;
}

export class QuoteDto {
  @IsNotEmpty()
  @IsString()
  amount: string;

  @IsNotEmpty()
  @IsNumber()
  estimatedGas: number;
}
