// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
	base: '/',
	integrations: [
		starlight({
			title: 'BizHealth Docs Hub',
			defaultLocale: 'ko',
			locales: {
				root: { label: '한국어', lang: 'ko' },
			},
			sidebar: [
				{
					label: '대시보드 기획',
					items: [
						{ label: '추진 배경 및 목적', link: '/dashboard/background/' },
						{ label: '효율/수익 지표 정의', link: '/dashboard/efficiency-profit/' },
						{ label: 'VoC 개발 요청서', link: '/dashboard/voc-request/' },
						{ label: '업무 추진 현황 ↗', link: '/files/dashboard_progress_20260521.html', attrs: { target: '_blank' } },
						{ label: '화면 설계 · 와이어프레임', link: '/dashboard/wireframes/' },
						{ label: '파일 다운로드', link: '/dashboard/downloads/' },
					],
				},
				{
					label: 'Medallia 사례 분석',
					items: [
						{ label: '발표 슬라이드 ↗', link: '/files/medallia_presentation.html', attrs: { target: '_blank' } },
						{ label: '미팅 요약', link: '/medallia/meeting-summary/' },
						{ label: '분석 보고서 모음', link: '/medallia/reports/' },
					],
				},
				{
					label: '가이드 & 도구',
					items: [
						{ label: 'AI 워크플로우 슬라이드 ↗', link: '/files/ai_research_workflow_slides.html', attrs: { target: '_blank' } },
						{ label: 'AI 워크플로우 문서 ↗', link: '/files/ai_research_workflow.html', attrs: { target: '_blank' } },
						{ label: '보고서 기준 v2.0', link: '/guides/analysis-report/' },
						{ label: '보고서 서식 가이드', link: '/guides/report-format/' },
						{ label: 'SDS Word Writer', link: '/guides/sds-word-writer/' },
					],
				},
				{
					label: '📂 파일 업로드',
					link: '/html/upload.html',
					attrs: { target: '_blank' },
				},
			],
		}),
	],
});
