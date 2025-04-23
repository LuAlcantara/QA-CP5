import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    vus: 50,
    duration: '1m',
    thresholds: {
        http_req_duration: ['p(95)<1500'],
        http_req_failed: ['rate<0.05'],
    },
};

const url = 'http://localhost:3003/api/room';

export default function () {
    if (Math.random() < 0.7) {
        // GET
        const res = http.get(url);
        check(res, { 'GET status is 200': (r) => r.status === 200 });
    } else {
        // POST
        const payload = JSON.stringify({
            roomName: `Quarto ${__VU}-${__ITER}`,
            type: "Single",
            accessible: true,
            image: "https://via.placeholder.com/150",
            description: "Teste de performance",
            features: ["WiFi"]
        });
        const params = { headers: { 'Content-Type': 'application/json' } };
        const res = http.post(url, payload, params);
        check(res, { 'POST status is 201': (r) => r.status === 201 });
    }
    sleep(1);
}
