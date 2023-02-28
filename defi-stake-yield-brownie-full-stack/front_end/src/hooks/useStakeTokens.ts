import { useEffect, useState } from "react"
import { useEthers, useContractFunction } from "@usedapp/core"
import { constants, utils } from "ethers"
import TokenFarm from "../chain-info/contracts/TokenFarm.json"
import ERC20 from "../chain-info/contracts/MockERC20.json"
import { Contract } from "@ethersproject/contracts"
import networkMapping from "../chain-info/deployments/map.json"

export const useStakeTokens = (tokenAddress: string) => {
    // address
    // abi
    // chainId
    const { chainId } = useEthers()
    const { abi } = TokenFarm
    const tokenFarmContractAddress = chainId ? networkMapping[String(chainId)]["TokenFarm"][0] : constants.AddressZero

    const tokenFarmInterface = new utils.Interface(abi)

    const tokenFarmContract = new Contract(
        tokenFarmContractAddress,
        tokenFarmInterface
      )

    const { send: stakeTokensSend, state: stakeTokensState } =
        useContractFunction(tokenFarmContract, "stakeTokens", {
          transactionName: "Stake tokens",
        })

    const erc20Interface = new utils.Interface(ERC20.abi)

    const tokenContract = new Contract(tokenAddress, erc20Interface)

    const { send: approveErc20Send, state: approveErc20State } =
        useContractFunction(tokenContract, "approve", {
          transactionName: "Approve ERC20 transfer",
        })

    const [amountToStake, setAmountToStake] = useState("0")

    useEffect(() => {
        if (approveErc20State.status === "Success") {
          stakeTokensSend(amountToStake, tokenAddress)
        }
        // the dependency arry
        // the code inside the useEffect anytime
        // anything in this list changes
        // if you want something to run when the component first runs
        // you just have a blank list
      }, [approveErc20State, amountToStake, tokenAddress]) // eslint-disable-line react-hooks/exhaustive-deps

    const send = (amount: string) => {
        setAmountToStake(amount)
        return approveErc20Send(tokenFarmContractAddress, amount)
    }

    const [state, setState] = useState(approveErc20State)

    useEffect(() => {
       if (approveErc20State.status === "Success") {
          setState(stakeTokensState)
       } else {
         setState(approveErc20State)
       }
    }, [approveErc20State, stakeTokensState])

    return { send, state }
}