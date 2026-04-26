import { createApp } from 'vue';
import { vMoney } from 'v-money';
import { VueMaskDirective } from 'v-mask';

import ProductCreate from './ProductCreateForm.vue';

const app = createApp(ProductCreate);

app.directive('mask', VueMaskDirective);
app.directive('money', vMoney);

app.mount('#product-create-app');