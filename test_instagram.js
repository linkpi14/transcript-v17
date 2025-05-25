// Script de teste para a funcionalidade do Instagram
import axios from 'axios';

async function testInstagramTranscription() {
  try {
    const response = await axios.post('http://localhost:3001/api/transcribe-instagram', {
      url: 'https://www.instagram.com/reel/SEU_CODIGO_AQUI',
      language: 'pt', // ou 'auto' para detecção automática
      shouldTranslate: true,
      shouldFormat: true
    });

    console.log('Resultado:', response.data);
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}

testInstagramTranscription(); 
