// ProdutoForm.tsx
import React, { useState } from 'react';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/produtos/';

function ProdutoForm() {
  const [nome, setNome] = useState('');
  const [categoria, setCategoria] = useState('');
  const [preco, setPreco] = useState('');
  const [quantidade_em_estoque, setQuantidade_em_estoque] = useState('');

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const dados = {
      nome,
      categoria,
      preco,
      quantidade_em_estoque,
    };

    try {
      const response = await axios.post(`${API_URL}`, dados);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="nome">Nome:</label>
      <input type="text" id="nome" value={nome} onChange={(event) => setNome(event.target.value)} />
      <br />
      <label htmlFor="categoria">Categoria:</label>
      <input type="text" id="categoria" value={categoria} onChange={(event) => setCategoria(event.target.value)} />
      <br />
      <label htmlFor="preco">Preço:</label>
      <input type="number" id="preco" value={preco} onChange={(event) => setPreco(event.target.value)} />
      <br />
      <label htmlFor="quantidade_em_estoque">Quantidade em Estoque:</label>
      <input type="number" id="quantidade_em_estoque" value={quantidade_em_estoque} onChange={(event) => setQuantidade_em_estoque(event.target.value)} />
      <br />
      <button type="submit">Cadastrar</button>
    </form>
  );
}

export default ProdutoForm;