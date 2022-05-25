--
-- PostgreSQL database dump
--

-- Dumped from database version 14.3 (Ubuntu 14.3-1.pgdg22.04+1)
-- Dumped by pg_dump version 14.3 (Ubuntu 14.3-1.pgdg22.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: mood; Type: TYPE; Schema: public; Owner: matej
--

CREATE TYPE public.mood AS ENUM (
    'sad',
    'good',
    'great'
);


ALTER TYPE public.mood OWNER TO matej;

--
-- Name: jobs_update(); Type: FUNCTION; Schema: public; Owner: matej
--

CREATE FUNCTION public.jobs_update() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
begin
   new.updated_on = now();
   return new;
end;
$$;


ALTER FUNCTION public.jobs_update() OWNER TO matej;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: jobs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jobs (
    name character varying(255) NOT NULL,
    salary money,
    updated_on timestamp without time zone DEFAULT now()
);


ALTER TABLE public.jobs OWNER TO postgres;

--
-- Name: people; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.people (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    age integer,
    job character varying(255) NOT NULL,
    joined timestamp without time zone,
    birthday date,
    current_mood public.mood
);


ALTER TABLE public.people OWNER TO postgres;

--
-- Name: persons_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.persons_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.persons_id_seq OWNER TO postgres;

--
-- Name: persons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.persons_id_seq OWNED BY public.people.id;


--
-- Name: people id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.people ALTER COLUMN id SET DEFAULT nextval('public.persons_id_seq'::regclass);


--
-- Data for Name: jobs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jobs (name, salary, updated_on) FROM stdin;
IT	10 000,00 Kč	2022-05-25 09:00:57.74178
Seller	20 000,00 Kč	2022-05-25 09:00:57.74178
Manager	30 000,00 Kč	2022-05-25 09:00:57.74178
Lawyer	50 000,00 Kč	2022-05-25 09:14:46.460532
\.


--
-- Data for Name: people; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.people (id, name, age, job, joined, birthday, current_mood) FROM stdin;
1	Matej	24	IT	2022-05-24 09:27:01.69267	1998-03-07	good
2	Jan	17	Seller	2022-05-24 09:27:12.919558	1994-04-07	good
3	Anna	35	Manager	2022-05-24 09:27:18.275579	1968-11-23	sad
4	Hana	62	IT	2022-05-24 09:27:24.711319	2006-12-24	great
\.


--
-- Name: persons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.persons_id_seq', 17, true);


--
-- Name: jobs jobs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jobs
    ADD CONSTRAINT jobs_pkey PRIMARY KEY (name);


--
-- Name: people persons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.people
    ADD CONSTRAINT persons_pkey PRIMARY KEY (id);


--
-- Name: jobs update_jobs_timestamp; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER update_jobs_timestamp BEFORE UPDATE ON public.jobs FOR EACH ROW EXECUTE FUNCTION public.jobs_update();


--
-- Name: people persons_job_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.people
    ADD CONSTRAINT persons_job_fkey FOREIGN KEY (job) REFERENCES public.jobs(name);


--
-- PostgreSQL database dump complete
--

