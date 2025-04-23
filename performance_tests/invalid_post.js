import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    vus: 50,
    duration: '1m',
    thresholds: {
        http_req_failed: ['rate<0.5'], // Espera-se alta taxa de erro, mas não 100%
    },
};

const url = 'http://localhost:3003/api/room';

export default function () {
    const payload = JSON.stringify({
        type: "Single",
        accessible: true
        // roomName ausente (inválido)
    });
    const params = { headers: { 'Content-Type': 'application/json' } };
    const res = http.post(url, payload, params);
    check(res, { 'POST status is 400': (r) => r.status === 400 });
    sleep(1);
}
