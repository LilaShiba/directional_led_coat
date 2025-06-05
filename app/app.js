const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const angleSlider = document.getElementById('angleSlider');
const angleValue = document.getElementById('angleValue');

const centerX = canvas.width / 2;
const centerY = canvas.height / 2;
const radius = 200;

function drawCircle(angleDeg) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw unit circle
  ctx.strokeStyle = '#888';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
  ctx.stroke();

  // Draw axes
  ctx.strokeStyle = '#444';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(centerX, 0);
  ctx.lineTo(centerX, canvas.height);
  ctx.moveTo(0, centerY);
  ctx.lineTo(canvas.width, centerY);
  ctx.stroke();

  const angleRad = angleDeg * Math.PI / 180;
  const x = Math.cos(angleRad);
  const y = Math.sin(angleRad);

  // Draw radius line (green)
  ctx.strokeStyle = '#0f0';
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(centerX, centerY);
  ctx.lineTo(centerX + x * radius, centerY - y * radius);
  ctx.stroke();

  // Draw cosine (blue)
  ctx.strokeStyle = '#09f';
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(centerX, centerY);
  ctx.lineTo(centerX + x * radius, centerY);
  ctx.stroke();

  // Draw sine (red)
  ctx.strokeStyle = '#f33';
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(centerX + x * radius, centerY);
  ctx.lineTo(centerX + x * radius, centerY - y * radius);
  ctx.stroke();

  // Draw tangent (yellow) if defined
  if (Math.abs(x) > 0.01) {
    ctx.strokeStyle = '#ff0';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(centerX + x * radius, centerY);
    ctx.lineTo(centerX + x * radius, centerY - (y / x) * radius);
    ctx.stroke();
  }

  // Draw point on circle
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.arc(centerX + x * radius, centerY - y * radius, 6, 0, 2 * Math.PI);
  ctx.fill();
}

angleSlider.addEventListener('input', () => {
  const angle = parseInt(angleSlider.value);
  angleValue.textContent = angle;
  drawCircle(angle);
});

drawCircle(0);
