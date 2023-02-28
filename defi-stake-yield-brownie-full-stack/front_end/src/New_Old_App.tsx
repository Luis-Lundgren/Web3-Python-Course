import React from 'react'
import { Kovan, ChainId, DAppProvider } from "@usedapp/core"
import { Header } from "./component/Header"
import { Container } from "@material-ui/core"
import { Main } from "./component/Main"

function App() {
  return (
    <DAppProvider config={{
      // supportedChains: [ChainId.Kovan],
      notifications: {
        expirationPeriod: 1000,
        checkInterval: 1000
      }
    }}>
      <Header />
      <Container maxWidth="md">
        <Main />
      </Container>
    </DAppProvider>
  )
}

export default App