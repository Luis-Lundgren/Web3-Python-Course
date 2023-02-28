import React from 'react';
import { Kovan, DAppProvider, ChainId } from "@usedapp/core"
import { Header } from "./component/Header"
import { Container } from "@material-ui/core"
import { Main } from "./component/Main"

function App() {
  return (
  <DAppProvider config={{

  }}>
    <Header />
    <Container maxWidth="md">
        <div>Hi!</div>
            <Main />
    </Container>
   </DAppProvider>
  );
}

export default App;
