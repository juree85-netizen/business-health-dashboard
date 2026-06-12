// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
	integrations: [
		starlight({
			title: 'VERA HUB',
			defaultLocale: 'ko',
			locales: {
				root: { label: '한국어', lang: 'ko' },
			},
			description: '유주리의 업무 정체성 · 커리어 아카이브',
			sidebar: [
				{
					label: '나를 정의하는 것들',
					items: [
						{ label: '정체성 프로필 (4축)', link: '/profile/identity/' },
						{ label: '한 줄 자기소개', link: '/profile/intro/' },
					],
				},
				{
					label: '직장 이력',
					items: [
						{ label: '현대자동차 (2008–2018)', link: '/career/hyundai/' },
						{ label: '삼성SDS (2018–현재)', link: '/career/samsung-sds/' },
					],
				},
				{
					label: '커리어 방향',
					items: [
						{ label: '커리어 타임라인', link: '/career/timeline/' },
						{ label: '되고 싶은 전문가상', link: '/career/vision/' },
					],
				},
				{
					label: '상황별 포지셔닝',
					items: [
						{ label: '발표·보고용 소개', link: '/positioning/presentation/' },
						{ label: '강점 요약', link: '/positioning/strengths/' },
					],
				},
			],
		}),
	],
});
