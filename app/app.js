const canvas     = document.getElementById('canvas');
const ctx        = canvas.getContext('2d');
const slider     = document.getElementById('angleSlider');
const angleLabel = document.getElementById('angleValue');

const CX = canvas.width  / 2;
const CY = canvas.height / 2;
const R  = 200;

function drawCircle(angleDeg) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const θ = angleDeg * Math.PI / 180;
  const x = Math.cos(θ);
  const y = Math.sin(θ);

  // Unit circle
  ctx.strokeStyle = '#555';
  ctx.lineWidth   = 2;
  ctx.beginPath();
  ctx.arc(CX, CY, R, 0, 2 * Math.PI);
  ctx.stroke();

  // Axes
  ctx.strokeStyle = '#333';
  ctx.lineWidth   = 1;
  ctx.beginPath();
  ctx.moveTo(CX, 0);
  ctx.lineTo(CX, canvas.height);
  ctx.moveTo(0, CY);
  ctx.lineTo(canvas.width, CY);
  ctx.stroke();

  // Radius (I)
  ctx.strokeStyle = '#0f0';
  ctx.lineWidth   = 3;
  ctx.beginPath();
  ctx.moveTo(CX, CY);
  ctx.lineTo(CX + x * R, CY - y * R);
  ctx.stroke();
  ctx.fillText('I: radius', CX + x * R + 10, CY - y * R - 10);

  // Cosine (II)
  ctx.strokeStyle = '#09f';
  ctx.lineWidth   = 3;
  ctx.beginPath();
  ctx.moveTo(CX, CY);
  ctx.lineTo(CX + x * R, CY);
  ctx.stroke();
  ctx.fillText('II: cos θ', CX + x * R / 2 - 20, CY + 15);

  // Sine (III)
  ctx.strokeStyle = '#f33';
  ctx.lineWidth   = 3;
  ctx.beginPath();
  ctx.moveTo(CX + x * R, CY);
  ctx.lineTo(CX + x * R, CY - y * R);
  ctx.stroke();
  ctx.fillText('III: sin θ', CX + x * R + 5, CY - y * R / 2);

  // Tangents if cos≠0
  if (Math.abs(x) > Number.EPSILON) {
    const tanLen = (y / x) * R;

    // Vertical at x-axis
    ctx.strokeStyle = '#ff0';
    ctx.lineWidth   = 2;
    ctx.beginPath();
    ctx.moveTo(CX + x * R, CY);
    ctx.lineTo(CX + x * R, CY - tanLen);
    ctx.stroke();
    ctx.fillText('tan θ @ x-axis', CX + x * R + 5, CY - tanLen - 5);

    // Through origin (dashed)
    ctx.save();
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.moveTo(CX, CY);
    const scale = 1 / x;  // sec θ
    ctx.lineTo(
      CX + x * R * scale,
      CY - y * R * scale
    );
    ctx.stroke();
    ctx.restore();
    ctx.fillText('tan θ from origin', CX + x * R * scale + 5, CY - y * R * scale - 5);
  }

  // Point on circle
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.arc(CX + x * R, CY - y * R, 6, 0, 2 * Math.PI);
  ctx.fill();
}

slider.addEventListener('input', () => {
  const a = +slider.value;
  angleLabel.textContent = a + '°';
  drawCircle(a);
});

// Initial draw
drawCircle(+slider.value);
