<script setup lang="ts">
import { ref } from 'vue';
import { computed } from 'vue';
import { getPrimary, getSecondary } from '@/utils/UpdateColors';
import { useTheme } from 'vuetify';
// common components
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';
import UiChildCard from '@/components/shared/UiChildCard.vue';
// theme breadcrumb
const page = ref({ title: '' });

const theme = useTheme();
const success = theme.current.value.colors.success;
const accent = theme.current.value.colors.accent;
const warning = theme.current.value.colors.warning;

const radialBarchartOptions = computed(() => {
    return {
        chart: {
            type: 'radialBar',
            height: 300,
            fontFamily: `inherit`,
            foreColor: '#adb0bb',
            toolbar: {
                show: false
            }
        },
        colors: ['#6ac3fd', '#0b70fb', '#f64e60', '#ffa800'],
        plotOptions: {
            radialBar: {
                dataLabels: {
                    name: {
                        fontSize: '22px'
                    },
                    value: {
                        fontSize: '16px'
                    },
                    total: {
                        show: true,
                        label: 'Total',
                        formatter() {
                            return 249;
                        }
                    }
                }
            }
        },
    };
});

const radialBarChart = {
    series: [44, 55, 67, 83]
};

const radarOptions = computed(() => {
    return {
        chart: {
            type: 'radar',
            height: 300,
            fontFamily: `inherit`,
             toolbar: {
                    show: false,
                },
        },
        colors: ['#0b70fb'],
        labels: ['January', 'February', 'March', 'April', 'May', 'June'],
    };
});

const radarChart = {
    series: [
        {
            name: 'Sales',
            data: [80, 50, 30, 40, 100, 20],
        }
    ]
};
</script>

<template>
    <v-row>
        <v-col cols="12">
            <v-row>
                <v-col cols="12" lg="6">
                    <!-- ---------------------------------------------------- -->
                    <!-- Radialbar Chart -->
                    <!-- ---------------------------------------------------- -->
                    <UiChildCard title="Porcentaje Parcial de Seguimiento" class="bg-surface">
                        <apexchart type="radialBar" height="300" :options="radialBarchartOptions" :series="radialBarChart.series">
                        </apexchart>
                    </UiChildCard>
                </v-col>
                <v-col cols="12" lg="6">
                    <!-- ---------------------------------------------------- -->
                    <!-- Radar Chart -->
                    <!-- ---------------------------------------------------- -->
                    <UiChildCard title="Diferencia de Seguimiento" class="bg-surface">
                        <apexchart type="radar" height="300" :options="radarOptions" :series="radarChart.series"> </apexchart>
                    </UiChildCard>
                </v-col>
            </v-row>
        </v-col>
    </v-row>
</template>
