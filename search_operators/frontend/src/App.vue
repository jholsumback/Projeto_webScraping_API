<template>
  <div class="container">
    <h1>🔍 Busca de Operadoras</h1>

    <input
      v-model="searchQuery"
      @keyup.enter="fetchOperators"
      type="text"
      placeholder="Digite um termo de pesquisa..."
      class="search-input"
    />

    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th v-for="key in keys" :key="key">
              {{ formatKey(key) }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(operator, index) in operators" :key="index">
            <td class="text-color" v-for="key in keys" :key="key">
              {{ operator[key] || '—' }}
            </td>
          </tr>
          <tr v-if="operators.length === 0">
            <td colspan="3" class="no-results">Nenhum resultado encontrado.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'


const operators = ref([])
const keys = ref([])
const searchQuery = ref('')

const fetchOperators = async () => {
  try {
    const response = await fetch('http://localhost:8000/search?query='+searchQuery.value)
    operators.value = await response.json()
    if (operators.value.length > 0) {
      keys.value = Object.keys(operators.value[0])
    }
  } catch (error) {
    console.error('Erro ao buscar usuários:', error)
  }
}
function formatKey(key) {
  return key
    .replace(/_/g, ' ')
    .replace(/\b\w/g, l => l.toUpperCase())
}

</script>

<style scoped>
/* Container */
.container {
  
 
  padding: 40px 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f7f9fc;
}

/* Título */
h1 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 30px;
  color: #333;
}

/* Campo de busca */
.search-input {
  width: 100%;
  padding: 12px 16px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 12px;
  margin-bottom: 30px;
  transition: border-color 0.3s ease;
}

.search-input:focus {
  border-color: #007BFF;
  outline: none;
}

/* Tabela */
.table-container {
  overflow-x: auto;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.text-color{
  color: black;
}

table {
  width: 100%;
  border-collapse: collapse;
  border-radius: 12px;
  overflow: hidden;
}

thead {
  background-color: #e9f0f7;
}

th, td {
  text-align: left;
  padding: 14px 20px;
  border-bottom: 1px solid #ddd;
}

tr:hover {
  background-color: #f1f8ff;
  transition: background-color 0.2s ease;
}

th {
  font-weight: 600;
  color: #333;
}

.no-results {
  text-align: center;
  padding: 20px;
  color: #888;
  font-style: italic;
}
</style>
