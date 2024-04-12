# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).
<!-- ### Solution: -->
>Following is my profitable path:\
\
<font color="green"> Initial tokenB balance: 5</font>\
<font color="green"> tokenB -> tokenA: 5.655321988655322</font>\
<font color="green">- tokenA -> tokenD: 2.4587813170979333</font>\
<font color="green">-- tokenD -> tokenC: 5.0889272933015155</font>\
<font color="green">--- tokenC -> tokenB: 20.129888944077443</font>\
\
Path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.129888944077443

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.
<!-- ### Solution: -->
>Slippage occurs when the final price of a trade in an Automated Market Maker (AMM) like Uniswap V2 differs from the expected price at trade initiation. Uniswap V2 combats this by allowing users to set a minimum amount they're willing to accept, controlling maximum slippage.\
The fundamental formula Uniswap V2 uses, ignoring fees for simplicity, is `x * y = k`, where `x` and `y` are token reserves, and `k` remains constant. This ensures the product of the reserves remains constant post-trade, affecting the pool's price.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?
<!-- ### Solution: -->
>Uniswap V2 locks a minimum liquidity amount (typically 1000 liquidity tokens) to prevent manipulation by early liquidity providers. This "seed" liquidity ensures fair distribution of transaction fees and stabilizes initial pool pricing.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?
<!-- ### Solution: -->
>The liquidity minted when adding to an existing pool is proportional to the contributor's share. This maintains fair fee distribution and is calculated as `L = min(amount0 / reserve0, amount1 / reserve1) * totalsupply`, keeping ownership percentages consistent.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?
<!-- ### Solution: -->
>A sandwich attack is when an attacker uses a pending swap seen in the mempool to manipulate token prices for profit. They execute a trade before and after the victim's transaction, impacting the victim's swap outcome. Users can mitigate this by setting tighter slippage tolerances and using protocols with front-running protections.

