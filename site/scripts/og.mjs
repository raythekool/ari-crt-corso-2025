import sharp from 'sharp';
import { fileURLToPath } from 'node:url';

const svg = fileURLToPath(new URL('../public/og.svg', import.meta.url));
const png = fileURLToPath(new URL('../public/og.png', import.meta.url));
await sharp(svg).png().toFile(png);