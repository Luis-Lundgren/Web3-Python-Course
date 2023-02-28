import { Token } from "../Main"
import { useEthers, useTokenBalance } from "@usedapp/core"
import { formatUnits } from "@ethersproject/units"
// eslint-disable-next-line
// import { BalanceMsg } from "../../component/BalanceMsg"

export interface WalletBalanceProps {
    token: Token
}

export const WalletBalance = ({ token }: WalletBalanceProps) => {
    const { image, address, name } = token
    const DAI_ADDRESS = '0xFab46E002BbF0b4509813474841E0716E6730136'
    const { account } = useEthers()
//     const tokenBalance = useTokenBalance(address, account)
    console.log(account)
    const daiBalance = useTokenBalance(DAI_ADDRESS, account)
    console.log(daiBalance?.toString())
    const formattedTokenBalance: number = daiBalance ? parseFloat(formatUnits(daiBalance, 18)) : 0
//     console.log(tokenBalance?.toString())
//     const formattedTokenBalance: number = tokenBalance ? parseFloat(formatUnits(tokenBalance, 18)) : 0
    return (<div>{formattedTokenBalance}</div>)
}