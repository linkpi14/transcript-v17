import { spawn } from 'child_process';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Verificar Python
const python = spawn('python3', ['--version']);
python.stdout.on('data', (data) => {
  console.log('Python version:', data.toString());
});

// Verificar caminhos
console.log('Current directory:', process.cwd());
console.log('__dirname:', __dirname);

// Verificar se o script do Instagram existe
const pythonScript = path.join(__dirname, 'src', 'instagram_downloader.py');
console.log('Python script path:', pythonScript);
console.log('Python script exists:', fs.existsSync(pythonScript));

// Listar conteúdo do diretório src
const srcDir = path.join(__dirname, 'src');
if (fs.existsSync(srcDir)) {
  console.log('Contents of src directory:', fs.readdirSync(srcDir));
} else {
  console.log('src directory does not exist');
} 