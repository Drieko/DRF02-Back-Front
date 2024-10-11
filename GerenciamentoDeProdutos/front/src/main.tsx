import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import ProdutoForm from './ProdutoForm'; // Importe o componente ProdutoForm

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ProdutoForm />
  </StrictMode>,
)
