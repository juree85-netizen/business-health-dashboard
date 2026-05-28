// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
	base: '/',
	integrations: [
		starlight({
			title: 'Biz Healthcheck Dashboard',
			defaultLocale: 'ko',
			locales: {
				root: { label: '한국어', lang: 'ko' },
			},
			sidebar: [
				{
					label: '대시보드 기획',
					autogenerate: { directory: 'dashboard' },
				},
				{
					label: 'Medallia 사례 분석',
					autogenerate: { directory: 'medallia' },
				},
				{
					label: '가이드 & 도구',
					autogenerate: { directory: 'guides' },
				},
				{
					label: 'HTML 자료',
					items: [
						{ label: '발표자료 & 분석 보고서', link: '/html-docs/presentation/' },
						{ label: '와이어프레임', link: '/html-docs/wireframes/' },
						{ label: '개발 요청서 & 기획 문서', link: '/html-docs/dev-requests/' },
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
