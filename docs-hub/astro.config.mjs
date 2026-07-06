// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
	site: 'https://juree85-netizen.github.io',
	base: process.env.BASE_PATH || '/',
	integrations: [
		starlight({
			title: 'PLAN HUB',
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
						{ label: '업무 추진 현황', link: '/dashboard/progress/' },
						{ label: '화면 설계 · 와이어프레임', link: '/dashboard/wireframes/' },
						{ label: '파일 다운로드', link: '/dashboard/downloads/' },
					],
				},
				{
					label: '대시보드 운영',
					items: [
						{
							label: '수작업 데이터 업로드',
							items: [
								{ label: '시장 데이터 변환 파일', link: '/operations/manual-upload/' },
								{ label: '파일 업로드', link: '/operations/upload/' },
							],
						},
					],
				},
				{
					label: '기업 분석 보고서',
					items: [
						{
							label: 'Medallia',
							items: [
								{ label: '분석 보고서 모음', link: '/medallia/reports/' },
								{ label: '미팅 요약', link: '/medallia/meeting-summary/' },
								{ label: '발표자료', link: '/medallia/slides/' },
							],
						},
						{
							label: 'Coupa',
							items: [
								{ label: '투자·M&A 관점 분석', link: '/project/coupa-investment/' },
								{ label: 'tuck-in 전략 분석 (v2)', link: '/project/coupa-strategy-v2/' },
								{ label: 'Rossum 인수 분석', link: '/project/coupa-rossum/' },
								{ label: 'Rossum 사업부장 보고 (2026.6.22)', link: '/project/coupa-rossum-report-20260622/' },
								{ label: 'Rossum 피드백 정리 (2026.6.22)', link: '/project/coupa-rossum-feedback-20260622/' },
								{ label: 'Rossum 인수 분석 v3 — 검증수정본 (2026.7.3)', link: '/project/coupa-rossum-report-v2-20260623/' },
								{ label: 'Thoma Bravo — 기업 분석', link: '/project/thoma-bravo/' },
							],
						},
						{
							label: '기타',
							items: [
								{ label: '재무 지표 해설 — EBITDA·FCF Waterfall', link: '/project/financial-metrics-guide/' },
								{ label: '기업가치 평가 · M&A 인수가액 · PPA 해설', link: '/project/ma-valuation-guide/' },
							],
						},
					],
				},
				{
					label: '기획 프레임워크 스킬',
					items: [
						{ label: '01 이해 — /concept-map', link: '/guides/concept-map-prompt/' },
						{ label: '02 포지셔닝 — /brand-house', link: '/guides/brand-house/' },
						{ label: '03 비즈니스 성장 및 작동원리 — /mental-model', link: '/guides/mental-model/' },
						{ label: '04 비즈니스 진단 — /business-diagnosis', link: '/guides/business-diagnosis/' },
						{ label: '05 전략 — /strategy-canvas', link: '/guides/strategy-canvas/' },
					],
				},
				{
					label: '보고서 생성 스킬',
					items: [
						{ label: '/corp-report 기업조사 분석 보고서', link: '/guides/corp-report/' },
						{ label: '/ma-report M&A 인수 분석 보고서', link: '/guides/ma-report/' },
					],
				},
				{
					label: '사업건전성 대시보드 웹 구축',
					items: [
						{ label: '추진 배경 및 목적', link: '/guides/ai-verify-background-purpose/' },
						{ label: '검증 프로젝트 구조서 (v1.1)', link: '/guides/ai-dashboard-project-charter/' },
						{ label: '검증 계획서 (v1.0)', link: '/guides/ai-dashboard-verification-plan/' },
						{ label: 'AIPro / FabriX 활용 과제 기술 검토서', link: '/guides/aipro-tech-review/' },
						{ label: 'AI Use Case PoC 슬라이드', link: '/guides/ai-usecase/' },
						{ label: '킥오프 브리핑', link: '/guides/ai-verify-project-briefing/' },
						{ label: '통합 구조도', link: '/guides/ai-verify-architecture/' },
					],
				},
				{
					label: 'AI 발표 자료',
					items: [
						{ label: 'AI 스킬과 기획의 단계', link: '/guides/ai-planner-skills/' },
						{ label: 'AI 워크플로우 슬라이드', link: '/guides/ai-workflow-slides/' },
						{ label: 'AI 워크플로우 문서', link: '/guides/ai-workflow-doc/' },
					],
				},
				{
					label: '작성 가이드 & 도구',
					items: [
						{ label: '보고서 기준 v2.0', link: '/guides/analysis-report/' },
						{ label: '보고서 서식 가이드', link: '/guides/report-format/' },
						{ label: 'SDS Word Writer', link: '/guides/sds-word-writer/' },
					],
				},
			],
		}),
	],
});
