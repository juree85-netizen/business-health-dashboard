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
					label: '대시보드 운영',
					items: [
						{
							label: '수작업 데이터 업로드',
							items: [
								{ label: '시장 데이터 변환 파일', link: '/operations/manual-upload/' },
							],
						},
						{ label: '파일 업로드', link: '/operations/upload/' },
					],
				},
				{
					label: '대시보드 기획',
					items: [
						{ label: '추진 배경 및 목적', link: '/dashboard/background/' },
						{ label: '효율/수익 지표 정의', link: '/dashboard/efficiency-profit/' },
						{ label: 'VoC 개발 요청서', link: '/dashboard/voc-request/' },
						{ label: '업무 추진 현황', link: '/dashboard/progress/' },
						{ label: '화면 설계 · 와이어프레임', link: '/dashboard/wireframes/' },
						{ label: '파일 다운로드', link: '/dashboard/downloads/' },
					],
				},
				{
					label: 'Medallia 사례 분석',
					items: [
						{ label: '발표 목차 (26.05.28)', link: '/medallia/agenda/' },
						{ label: '발표 슬라이드', link: '/medallia/slides/' },
						{ label: '미팅 요약', link: '/medallia/meeting-summary/' },
						{ label: '분석 보고서 모음', link: '/medallia/reports/' },
					],
				},
				{
					label: 'Coupa M&A 전략 분석',
					items: [
						{ label: '(신규) 투자·M&A 관점 분석', link: '/project/coupa-investment/' },
						{ label: '4건 tuck-in 전략 분석 (v2)', link: '/project/coupa-strategy-v2/' },
						{ label: 'Rossum 단독 분석 (v1)', link: '/project/coupa-rossum/' },
					],
				},
				{
					label: '기업조사 분석 보고서',
					items: [
						{ label: 'Thoma Bravo', link: '/project/thoma-bravo/' },
					],
				},
				{
					label: '가이드 & 도구',
					items: [
						{ label: '/corp-report 기업조사 스킬', link: '/guides/corp-report/' },
						{ label: 'AI 워크플로우 슬라이드', link: '/guides/ai-workflow-slides/' },
						{ label: 'AI 워크플로우 문서', link: '/guides/ai-workflow-doc/' },
						{ label: '보고서 기준 v2.0', link: '/guides/analysis-report/' },
						{ label: '보고서 서식 가이드', link: '/guides/report-format/' },
						{ label: 'SDS Word Writer', link: '/guides/sds-word-writer/' },
						{ label: '개념 설명 지형도 프롬프트', link: '/guides/concept-map-prompt/' },
					],
				},
			],
		}),
	],
});
