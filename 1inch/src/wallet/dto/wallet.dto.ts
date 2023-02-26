export class WalletRequestDto {
  fromTokenAddress: string;
  toTokenAddress: string;
  walletAddress: string;
  amount: string;
  mode: string;
  slippage?: number;
  private_key?: string;
}
