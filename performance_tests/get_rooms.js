import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    vus: 20,
    duration: '1m',
    thresholds: {
        http_req_duration: ['p(95)<1000'], // 95% das requisições em < 1s
        http_req_failed: ['rate<0.01'],   // < 1% de falhas
    },
};

export default function () {
    const res = http.get('http://localhost:3003/api/room');
    check(res, {
        'status is 200': (r) => r.status === 200,
    });
    sleep(1); // simula tempo de "pensar" do usuário
}
