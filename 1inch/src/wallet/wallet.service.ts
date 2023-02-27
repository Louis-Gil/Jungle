import { QuoteDto, WalletRequestDto } from './dto/wallet.dto';
import { Injectable } from '@nestjs/common';
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
    const {
      fromTokenAddress,
      toTokenAddress,
      walletAddress,
      mode,
      slippage,
      private_key,
    } = walletRequestDto;

    const result = [];
    // const remain = await this.oneInchApi('/approve/allowance', {
    //   tokenAddress: fromTokenAddress,
    //   walletAddress,
    // });

    const wallet = this.web3.eth.accounts.wallet.add(private_key);
    const { amount, estimatedGas } = await this.quote(walletRequestDto);
    console.log('after quote');

    if (fromTokenAddress != '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE') {
      const approve = await this.approve(fromTokenAddress, wallet, amount);
      result.push(approve);
    }

    const response = await this.oneInchApi('/swap', {
      fromTokenAddress,
      toTokenAddress,
      amount,
      fromAddress: wallet.address,
      slippage,
      disableEstimate: true,
    });

    console.log(response);
    response.tx.gas = 1000000;
    const transaction = await this.web3.eth.sendTransaction(response.tx);

    if (transaction.status) {
      console.log('Transaction success');
    } else {
      console.log('Transaction failed');
    }

    result.push(transaction);
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
    } catch (e) {
      console.log(e);
    }
  }

  async approve(tokenAddress, wallet, amount) {
    try {
      const approve = await this.oneInchApi('/approve/transaction', {
        tokenAddress,
        amount,
      });
      console.log(approve);

      approve.gas = 1000000;
      approve.from = wallet.address; //check

      const transaction = await this.web3.eth.sendTransaction(approve);
      console.log(transaction);
      if (transaction.status) {
        console.log('Transaction success');
      } else {
        console.log('Transaction failed');
      }
      return transaction;
    } catch (e) {
      console.log(e);
    }
  }

  async quote(WalletRequestDto: WalletRequestDto) {
    const { fromTokenAddress, toTokenAddress, walletAddress, amount, mode } =
      WalletRequestDto;
    const quoteDto = new QuoteDto();
    const quoteAmount = await this.oneInchApi('/quote', {
      fromTokenAddress,
      toTokenAddress,
      amount,
    });

    if (mode == 'fixed_from_amount') {
      quoteDto.amount = quoteAmount.toTokenAmount;
      quoteDto.estimatedGas = quoteAmount.estimatedGas;
    } else if (mode == 'fixed_to_amount') {
      quoteDto.amount = (
        quoteAmount.fromTokenAmount ** 2 /
        quoteAmount.toTokenAmount
      ).toString();
      quoteDto.estimatedGas = Math.max(
        240000,
        (quoteAmount.estimatedGas * quoteAmount.fromTokenAmount) /
          quoteAmount.toTokenAmount,
      );
    }

    return quoteDto;
  }
}
