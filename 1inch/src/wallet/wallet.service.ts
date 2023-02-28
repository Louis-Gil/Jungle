import { QuoteDto, WalletRequestDto } from './dto/wallet.dto';
import { Injectable, HttpException } from '@nestjs/common';
import axios from 'axios';
import { Web3Service } from 'nest-web3';

@Injectable()
export class WalletService {
  constructor(private readonly web3Service: Web3Service) {}

  web3 = this.web3Service.getClient('eth');
  chainId = 137;
  apiBaseUrl = 'https://api.1inch.io/v5.0/' + this.chainId;

  async getQuote(walletRequestDto: WalletRequestDto) {
    const quoteAmount: QuoteDto = await this.quote(walletRequestDto);
    return quoteAmount;
  }

  async postSwap(walletRequestDto: WalletRequestDto) {
    const { fromTokenAddress, toTokenAddress, slippage, private_key } =
      walletRequestDto;

    const result = [];
    const wallet = this.web3.eth.accounts.wallet.add(private_key);
    const { fromAmount, ...quoteDto } = await this.quote(walletRequestDto);

    if (fromTokenAddress != '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE') {
      const approve = await this.approve(fromTokenAddress, wallet, fromAmount);
      result.push(approve);
    }

    const response = await this.oneInchApi('/swap', {
      fromTokenAddress,
      toTokenAddress,
      amount: fromAmount,
      fromAddress: wallet.address,
      slippage,
      disableEstimate: true,
    });

    response.tx.gas = 1000000;
    const transaction = await this.web3.eth.sendTransaction(response.tx);
    result.push(transaction);

    if (transaction.status) {
      console.log('Transaction success');
    } else {
      console.log('Transaction failed');
    }
    return result;
  }

  async oneInchApi(methodName, queryParams) {
    try {
      const url =
        this.apiBaseUrl +
        methodName +
        '?' +
        new URLSearchParams(queryParams).toString();
      const { data } = await axios.get(url);
      return data;
    } catch (err) {
      throw new HttpException(`oneInchApi err : ${methodName}, ${err}`, 500);
    }
  }

  async approve(tokenAddress, wallet, amount) {
    try {
      const approve = await this.oneInchApi('/approve/transaction', {
        tokenAddress,
        amount,
      });
      approve.gas = 1000000;
      approve.from = wallet.address;

      const transaction = await this.web3.eth.sendTransaction(approve);
      if (transaction.status) {
        console.log('approve success');
      } else {
        console.log('approve failed');
      }
      return transaction;
    } catch (err) {
      throw new HttpException(`approve err : ${err}`, 500);
    }
  }

  async quote(WalletRequestDto: WalletRequestDto) {
    const { fromTokenAddress, toTokenAddress, amount, mode } = WalletRequestDto;
    const quoteDto = new QuoteDto();
    const quoteAmount = await this.oneInchApi('/quote', {
      fromTokenAddress,
      toTokenAddress,
      amount,
    });

    try {
      if (mode == 'fixed_from_amount') {
        quoteDto.fromAmount = amount;
        quoteDto.toAmount = quoteAmount.toTokenAmount;
        quoteDto.estimatedGas = quoteAmount.estimatedGas;
      } else if (mode == 'fixed_to_amount') {
        quoteDto.fromAmount = (
          Number(quoteAmount.fromTokenAmount) ** 2 /
          Number(quoteAmount.toTokenAmount)
        ).toString();
        quoteDto.toAmount = amount;
        quoteDto.estimatedGas = quoteAmount.estimatedGas;
      }

      if (toTokenAddress == '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE') {
        quoteDto.fromAmount = (Number(quoteDto.fromAmount) * 1.03).toString();
      }
      return quoteDto;
    } catch (error) {
      throw new HttpException(`quote err : ${error}`, 500);
    }
  }
}
