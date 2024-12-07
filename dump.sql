--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4
-- Dumped by pg_dump version 16.6 (Homebrew)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: animal; Type: TABLE; Schema: public; Owner: doadmin
--

CREATE TABLE public.animal (
    animal_id integer NOT NULL,
    owner_id integer,
    vet_id integer,
    name character varying(100) NOT NULL,
    last_name character varying(100),
    species character varying(100) NOT NULL,
    dob date,
    breed character varying(100) NOT NULL,
    color character varying(100) NOT NULL
);


ALTER TABLE public.animal OWNER TO doadmin;

--
-- Name: animal_animal_id_seq; Type: SEQUENCE; Schema: public; Owner: doadmin
--

CREATE SEQUENCE public.animal_animal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.animal_animal_id_seq OWNER TO doadmin;

--
-- Name: animal_animal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: doadmin
--

ALTER SEQUENCE public.animal_animal_id_seq OWNED BY public.animal.animal_id;


--
-- Name: history_bird; Type: TABLE; Schema: public; Owner: doadmin
--

CREATE TABLE public.history_bird (
    case_id integer NOT NULL,
    animal_id integer NOT NULL,
    vet_id integer,
    date_visit date,
    weight numeric,
    wingspan numeric,
    comment text,
    reason_visit text,
    wingclip boolean,
    flying_capacity text,
    cage_only boolean
);


ALTER TABLE public.history_bird OWNER TO doadmin;

--
-- Name: history_bird_case_id_seq; Type: SEQUENCE; Schema: public; Owner: doadmin
--

CREATE SEQUENCE public.history_bird_case_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.history_bird_case_id_seq OWNER TO doadmin;

--
-- Name: history_bird_case_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: doadmin
--

ALTER SEQUENCE public.history_bird_case_id_seq OWNED BY public.history_bird.case_id;


--
-- Name: history_cat; Type: TABLE; Schema: public; Owner: doadmin
--

CREATE TABLE public.history_cat (
    case_id integer NOT NULL,
    animal_id integer NOT NULL,
    vet_id integer,
    date_visit date,
    weight numeric,
    sterilization boolean,
    comment text,
    reason_visit text,
    in_outdoor boolean,
    food_passion character varying(100)
);


ALTER TABLE public.history_cat OWNER TO doadmin;

--
-- Name: history_cat_case_id_seq; Type: SEQUENCE; Schema: public; Owner: doadmin
--

CREATE SEQUENCE public.history_cat_case_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.history_cat_case_id_seq OWNER TO doadmin;

--
-- Name: history_cat_case_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: doadmin
--

ALTER SEQUENCE public.history_cat_case_id_seq OWNED BY public.history_cat.case_id;


--
-- Name: history_dog; Type: TABLE; Schema: public; Owner: doadmin
--

CREATE TABLE public.history_dog (
    case_id integer NOT NULL,
    animal_id integer NOT NULL,
    vet_id integer,
    date_visit date,
    weight numeric,
    sterilization boolean,
    comment text,
    reason_visit text,
    exercise_level character varying(100),
    food_passion character varying(100)
);


ALTER TABLE public.history_dog OWNER TO doadmin;

--
-- Name: history_dog_case_id_seq; Type: SEQUENCE; Schema: public; Owner: doadmin
--

CREATE SEQUENCE public.history_dog_case_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.history_dog_case_id_seq OWNER TO doadmin;

--
-- Name: history_dog_case_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: doadmin
--

ALTER SEQUENCE public.history_dog_case_id_seq OWNED BY public.history_dog.case_id;


--
-- Name: history_reptile; Type: TABLE; Schema: public; Owner: doadmin
--

CREATE TABLE public.history_reptile (
    case_id integer NOT NULL,
    animal_id integer NOT NULL,
    vet_id integer NOT NULL,
    date_visit date,
    weight numeric,
    length numeric,
    comment text,
    reason_visit text,
    housing_type character varying(100),
    temperature_keep numeric,
    humidity_keep numeric
);


ALTER TABLE public.history_reptile OWNER TO doadmin;

--
-- Name: history_reptile_case_id_seq; Type: SEQUENCE; Schema: public; Owner: doadmin
--

CREATE SEQUENCE public.history_reptile_case_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.history_reptile_case_id_seq OWNER TO doadmin;

--
-- Name: history_reptile_case_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: doadmin
--

ALTER SEQUENCE public.history_reptile_case_id_seq OWNED BY public.history_reptile.case_id;


--
-- Name: medical; Type: TABLE; Schema: public; Owner: doadmin
--

CREATE TABLE public.medical (
    medical_id integer NOT NULL,
    animal_id integer,
    symptoms character varying(255),
    treatment text,
    record_date date
);


ALTER TABLE public.medical OWNER TO doadmin;

--
-- Name: medical_medical_id_seq; Type: SEQUENCE; Schema: public; Owner: doadmin
--

CREATE SEQUENCE public.medical_medical_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.medical_medical_id_seq OWNER TO doadmin;

--
-- Name: medical_medical_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: doadmin
--

ALTER SEQUENCE public.medical_medical_id_seq OWNED BY public.medical.medical_id;


--
-- Name: medicine; Type: TABLE; Schema: public; Owner: doadmin
--

CREATE TABLE public.medicine (
    medicine_id integer NOT NULL,
    medical_id integer,
    animal_id integer,
    medicine_name character varying(100),
    doses integer,
    date_issue date
);


ALTER TABLE public.medicine OWNER TO doadmin;

--
-- Name: medicine_medicine_id_seq; Type: SEQUENCE; Schema: public; Owner: doadmin
--

CREATE SEQUENCE public.medicine_medicine_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.medicine_medicine_id_seq OWNER TO doadmin;

--
-- Name: medicine_medicine_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: doadmin
--

ALTER SEQUENCE public.medicine_medicine_id_seq OWNED BY public.medicine.medicine_id;


--
-- Name: owner; Type: TABLE; Schema: public; Owner: doadmin
--

CREATE TABLE public.owner (
    owner_id integer NOT NULL,
    name character varying(100) NOT NULL,
    email_address character varying(100) NOT NULL
);


ALTER TABLE public.owner OWNER TO doadmin;

--
-- Name: owner_owner_id_seq; Type: SEQUENCE; Schema: public; Owner: doadmin
--

CREATE SEQUENCE public.owner_owner_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.owner_owner_id_seq OWNER TO doadmin;

--
-- Name: owner_owner_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: doadmin
--

ALTER SEQUENCE public.owner_owner_id_seq OWNED BY public.owner.owner_id;


--
-- Name: vaccinations; Type: TABLE; Schema: public; Owner: doadmin
--

CREATE TABLE public.vaccinations (
    vaccine_id integer NOT NULL,
    animal_id integer,
    vaccine_name character varying(100),
    vaccine_date date,
    num_doses integer
);


ALTER TABLE public.vaccinations OWNER TO doadmin;

--
-- Name: vaccinations_vaccine_id_seq; Type: SEQUENCE; Schema: public; Owner: doadmin
--

CREATE SEQUENCE public.vaccinations_vaccine_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.vaccinations_vaccine_id_seq OWNER TO doadmin;

--
-- Name: vaccinations_vaccine_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: doadmin
--

ALTER SEQUENCE public.vaccinations_vaccine_id_seq OWNED BY public.vaccinations.vaccine_id;


--
-- Name: vet; Type: TABLE; Schema: public; Owner: doadmin
--

CREATE TABLE public.vet (
    vet_id integer NOT NULL,
    role character varying(50),
    username character varying(255) NOT NULL,
    password character varying(255) NOT NULL
);


ALTER TABLE public.vet OWNER TO doadmin;

--
-- Name: vet_vet_id_seq; Type: SEQUENCE; Schema: public; Owner: doadmin
--

CREATE SEQUENCE public.vet_vet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.vet_vet_id_seq OWNER TO doadmin;

--
-- Name: vet_vet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: doadmin
--

ALTER SEQUENCE public.vet_vet_id_seq OWNED BY public.vet.vet_id;


--
-- Name: animal animal_id; Type: DEFAULT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.animal ALTER COLUMN animal_id SET DEFAULT nextval('public.animal_animal_id_seq'::regclass);


--
-- Name: history_bird case_id; Type: DEFAULT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_bird ALTER COLUMN case_id SET DEFAULT nextval('public.history_bird_case_id_seq'::regclass);


--
-- Name: history_cat case_id; Type: DEFAULT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_cat ALTER COLUMN case_id SET DEFAULT nextval('public.history_cat_case_id_seq'::regclass);


--
-- Name: history_dog case_id; Type: DEFAULT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_dog ALTER COLUMN case_id SET DEFAULT nextval('public.history_dog_case_id_seq'::regclass);


--
-- Name: history_reptile case_id; Type: DEFAULT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_reptile ALTER COLUMN case_id SET DEFAULT nextval('public.history_reptile_case_id_seq'::regclass);


--
-- Name: medical medical_id; Type: DEFAULT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.medical ALTER COLUMN medical_id SET DEFAULT nextval('public.medical_medical_id_seq'::regclass);


--
-- Name: medicine medicine_id; Type: DEFAULT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.medicine ALTER COLUMN medicine_id SET DEFAULT nextval('public.medicine_medicine_id_seq'::regclass);


--
-- Name: owner owner_id; Type: DEFAULT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.owner ALTER COLUMN owner_id SET DEFAULT nextval('public.owner_owner_id_seq'::regclass);


--
-- Name: vaccinations vaccine_id; Type: DEFAULT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.vaccinations ALTER COLUMN vaccine_id SET DEFAULT nextval('public.vaccinations_vaccine_id_seq'::regclass);


--
-- Name: vet vet_id; Type: DEFAULT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.vet ALTER COLUMN vet_id SET DEFAULT nextval('public.vet_vet_id_seq'::regclass);


--
-- Data for Name: animal; Type: TABLE DATA; Schema: public; Owner: doadmin
--

COPY public.animal (animal_id, owner_id, vet_id, name, last_name, species, dob, breed, color) FROM stdin;
2	1	3	Whiskers	Doe	Cat	2019-03-15	Siamese	Cream
3	2	2	Bella	Smith	Dog	2020-01-22	Golden Retriever	Golden
4	2	4	Shadow	Smith	Cat	2020-05-22	Persian	Gray
5	3	3	Rocky	Johnson	Dog	2018-11-09	German Shepherd	Tan and Black
6	3	2	Mittens	Johnson	Cat	2018-08-30	Maine Coon	Brown
7	3	5	Iggy	Johnson	Reptile	2020-01-20	Iguana	Green
8	4	4	Spike	Davis	Reptile	2018-06-11	Bearded Dragon	Yellow
9	5	1	Polly	Brown	Bird	2016-04-15	Parrot	Green
10	5	2	Slither	Brown	Reptile	2019-09-30	Corn Snake	Red
1	1	1	Maxa	Doe	Dog	2017-05-12	Labrador	Black
60	8	1	Luna	Williams	Dog	2021-03-22	Border Collie	Black and White
61	9	5	Daisy	Brown	Cat	2022-06-16	Persian	White
62	10	5	Thor	Anderson	Dog	2019-11-11	Golden Retriever	Golden
63	11	4	Willow	Carter	Bird	2022-10-21	Parrot	Green and Red
64	12	3	Finn	Lee	Reptile	2017-10-18	Gecko	Orange
65	13	2	Milo	Robinson	Dog	2018-09-20	Pug	Fawn
66	14	1	Ruby	Harris	Cat	2019-05-12	Maine Coon	Gray and White
67	15	1	Hunter	Evans	Dog	2020-01-14	Siberian Husky	Black and White
68	16	2	Ziggy	Martin	Bird	2022-04-15	Budgerigar	Blue and Yellow
69	16	4	Blaze	Young	Reptile	2023-05-15	Iguana	Green
70	17	4	Stella	King	Dog	2023-09-24	Dachshund	Brown
71	18	3	Shadow	Scott	Cat	2018-10-14	British Shorthair	Black
72	19	3	Jasper	Wright	Dog	2020-07-22	Dalmatian	White with Spots
73	20	5	Pearl	Green	Bird	2018-01-18	Canary	Yellow
74	21	5	Echo	Adams	Reptile	2023-12-21	Chameleon	Multi-color
75	22	1	Diesel	Nelson	Dog	2016-11-21	Boxer	Brindle
76	23	2	Hazel	White	Cat	2022-06-15	Scottish Fold	Cream
77	24	3	Mango	Hall	Bird	2015-06-23	Cockatoo	White with Yellow
78	19	4	Titan	Allen	Reptile	2022-09-20	Tortoise	Brown and Yellow
79	23	5	Olive	Perez	Dog	2024-02-05	Beagle	Tri-color
\.


--
-- Data for Name: history_bird; Type: TABLE DATA; Schema: public; Owner: doadmin
--

COPY public.history_bird (case_id, animal_id, vet_id, date_visit, weight, wingspan, comment, reason_visit, wingclip, flying_capacity, cage_only) FROM stdin;
1	9	1	2024-05-15	0.5	25.0	Routine check-up	Annual health check	t	High	t
7	73	5	2022-06-22	5.0	25.0	Healthy	Routine health check	t	High	t
8	63	4	2023-06-21	2.0	45.0	Slight wing injury	Wing injury treatment	t	Excellent	f
9	77	3	2017-09-15	3.0	55.0	Young bird	Initial health check	f	\tVery Good	f
10	68	2	2024-06-17	3.0	55.0	Likes to sing a lot	Routine check-up	t	Good	f
\.


--
-- Data for Name: history_cat; Type: TABLE DATA; Schema: public; Owner: doadmin
--

COPY public.history_cat (case_id, animal_id, vet_id, date_visit, weight, sterilization, comment, reason_visit, in_outdoor, food_passion) FROM stdin;
1	2	3	2024-04-20	8.0	t	Routine check-up	Annual health check	t	Good
2	4	4	2024-05-18	9.5	f	Vaccination	Routine vaccination	f	Good
3	6	2	2024-06-12	11.0	t	Check-up	Behavioral issues	t	picky
7	61	5	2023-02-08	8.0	f	Very Good	General health assessment	f	Good
8	61	5	2024-02-19	13.0	f	Good	General health assessment	f	Good
9	66	1	2022-09-17	14.0	t	Shy	Routine check-up	t	Good
10	71	3	2021-01-03	16.0	t	Healthy	Routine check-up	t	Excellent
11	76	2	2023-08-21	10.0	t	Healthy and shy	Routine check-up	f	Median
\.


--
-- Data for Name: history_dog; Type: TABLE DATA; Schema: public; Owner: doadmin
--

COPY public.history_dog (case_id, animal_id, vet_id, date_visit, weight, sterilization, comment, reason_visit, exercise_level, food_passion) FROM stdin;
2	3	2	2024-06-10	40.0	t	Vaccination	Routine vaccination	Medium	Good
3	5	3	2024-07-15	35.0	f	Weight management	Weight monitoring	High	Good
1	1	1	2024-05-02	30.5	t	Routine check-up	Annual health check	High	Good
29	62	5	2019-12-04	20.0	t	Good	General health assessment	Median	Good
30	62	5	2020-06-16	25.0	t	Vaccine	Vaccination	Median	Good
31	79	5	2024-03-06	12.0	t	Friendly and active dog	Annual vaccination	High	Loves chicken treats
32	60	1	2023-06-12	20.0	f	Slightly overweight	Skin allergy check-up	Medium	Enjoys beef snacks
33	67	1	2022-05-17	25.0	f	Very energetic	Limping on front leg	Very High	Obsessed with bones
34	75	1	2022-05-17	30.0	t	Protective of owner	General health check	Medium	Loves canned food
35	70	4	2023-12-20	18.0	t	Gets anxious at vets	Vaccination booster	Medium	Enjoys liver treats
36	72	3	2021-01-03	40.0	f	Barking excessively	Behavior consultation	Low	Enjoys turkey slices
37	65	2	2022-10-20	60.0	f	Very obedient	Skin rash treatment	HIgh	Loves boiled eggs
\.


--
-- Data for Name: history_reptile; Type: TABLE DATA; Schema: public; Owner: doadmin
--

COPY public.history_reptile (case_id, animal_id, vet_id, date_visit, weight, length, comment, reason_visit, housing_type, temperature_keep, humidity_keep) FROM stdin;
1	7	5	2024-03-25	3.2	60.0	Routine health check	General health assessment	Terrarium	28.0	60.0
2	8	4	2024-07-05	0.8	30.0	Routine check-up	Skin shedding issue	Aquarium	25.0	50.0
3	10	2	2024-08-20	0.5	20.0	Routine check-up	Health assessment	Terrarium	22.0	45.0
5	74	5	2024-06-10	5.0	50.0	Healthy and active	Routine health check	Glass terrarium	28.0	60.0
6	69	4	2023-12-20	5.0	35.0	Aggressive behavior	Behavior assessment	Wooden vivarium	32.0	65.0
7	78	4	2024-05-06	4.0	40.0	Active and curious	Check on minor injury	Mesh enclosure	27.0	70.0
8	64	3	2022-07-13	3.0	30.0	Hatchling care	Initial health check	Wooden vivarium	28.0	68.0
\.


--
-- Data for Name: medical; Type: TABLE DATA; Schema: public; Owner: doadmin
--

COPY public.medical (medical_id, animal_id, symptoms, treatment, record_date) FROM stdin;
1	3	Excessive barking, anxiety	Behavioral therapy and training	2023-06-10
2	1	Coughing, sneezing	Antibiotics and rest	2023-05-01
3	6	Fever, lethargy	Fluid therapy and monitoring	2023-06-12
4	2	Skin irritation, scratching	Topical ointment and allergy meds	2023-04-20
5	4	Vomiting, lethargy	Diet change and hydration	2023-05-18
6	5	Eye discharge, squinting	Eye drops and cleaning	2023-07-15
7	7	Weight loss, reduced appetite	Nutritional supplements	2023-03-25
8	6	Vomiting	Require therapy	2024-12-04
9	7	Skin	Medicine	2024-12-04
\.


--
-- Data for Name: medicine; Type: TABLE DATA; Schema: public; Owner: doadmin
--

COPY public.medicine (medicine_id, medical_id, animal_id, medicine_name, doses, date_issue) FROM stdin;
1	2	1	Amoxicillin	10	2023-05-02
2	1	3	Fluoxetine	1	2023-06-11
3	4	2	Hydrocortisone Cream	1	2023-04-21
4	6	5	Cerenia	1	2023-07-16
5	3	6	Metronidazole	15	2023-06-13
\.


--
-- Data for Name: owner; Type: TABLE DATA; Schema: public; Owner: doadmin
--

COPY public.owner (owner_id, name, email_address) FROM stdin;
1	John Doe	john.doe@example.com
2	Jane Smith	jane.smith@example.com
3	Michael Johnson	michael.johnson@example.com
4	Emily Davis	emily.davis@example.com
5	Sarah Brown	sarah.brown@example.com
8	David	david.wilson@example.com
9	Emma	emma.thomas@example.com
10	James	james.moore@example.com
11	Olivia	olivia.taylor@example.com
12	Daniel	daniel.anderson@example.com
13	Sophia	sophia.martinez@example.com
14	Benjamin	benjamin.garcia@example.com
15	Ava	ava.rodriguez@example.com
16	Isabella	isabella.clark@example.com
17	Mason	mason.lopez@example.com
18	Logan	logan.adams@example.com
19	Harper	harper.lewis@example.com
20	Ethan	ethan.allen@example.com
21	Lily	lily.baker@example.com
22	Alexander	alexander.young@example.com
23	Charlotte	charlotte.scott@example.com
24	Amelia	amelia.green@example.com
\.


--
-- Data for Name: vaccinations; Type: TABLE DATA; Schema: public; Owner: doadmin
--

COPY public.vaccinations (vaccine_id, animal_id, vaccine_name, vaccine_date, num_doses) FROM stdin;
2	2	Feline Distemper Vaccine	2024-04-20	1
3	3	Canine Parvovirus Vaccine	2024-06-10	1
4	4	Feline Leukemia Vaccine	2024-05-18	1
5	5	Canine Bordetella Vaccine	2024-07-15	1
6	6	Feline Rabies Vaccine	2024-06-13	1
1	1	Rabies Vaccine	2024-05-01	1
11	60	Rabies Vaccine	2024-07-12	1
12	61	Feline Leukemia Virus (FeLV) Vaccine	2024-08-05	2
13	68	Avian Influenza Vaccine	2024-09-10	1
14	7	Reptile Adenovirus Vaccine	2024-05-15	1
15	77	Avian Pox Vaccine	2024-02-01	1
16	75	Canine Parainfluenza Vaccine	2024-12-04	1
17	66	Feline Viral Rhinotracheitis Vaccine	2024-05-17	1
18	9	Psittacosis Vaccine	2024-12-04	1
\.


--
-- Data for Name: vet; Type: TABLE DATA; Schema: public; Owner: doadmin
--

COPY public.vet (vet_id, role, username, password) FROM stdin;
2	Assistant	assistant.jane	securePass!456
3	Veterinarian	dr.emma_vet	VetPass789
4	Veterinarian	dr.michael_vet	secureVet007
5	Veterinary Nurse	nurse.sarah	safeNurse123
1	Veterinarian	dr.john_vet	password1234
\.


--
-- Name: animal_animal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: doadmin
--

SELECT pg_catalog.setval('public.animal_animal_id_seq', 79, true);


--
-- Name: history_bird_case_id_seq; Type: SEQUENCE SET; Schema: public; Owner: doadmin
--

SELECT pg_catalog.setval('public.history_bird_case_id_seq', 10, true);


--
-- Name: history_cat_case_id_seq; Type: SEQUENCE SET; Schema: public; Owner: doadmin
--

SELECT pg_catalog.setval('public.history_cat_case_id_seq', 11, true);


--
-- Name: history_dog_case_id_seq; Type: SEQUENCE SET; Schema: public; Owner: doadmin
--

SELECT pg_catalog.setval('public.history_dog_case_id_seq', 37, true);


--
-- Name: history_reptile_case_id_seq; Type: SEQUENCE SET; Schema: public; Owner: doadmin
--

SELECT pg_catalog.setval('public.history_reptile_case_id_seq', 8, true);


--
-- Name: medical_medical_id_seq; Type: SEQUENCE SET; Schema: public; Owner: doadmin
--

SELECT pg_catalog.setval('public.medical_medical_id_seq', 11, true);


--
-- Name: medicine_medicine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: doadmin
--

SELECT pg_catalog.setval('public.medicine_medicine_id_seq', 13, true);


--
-- Name: owner_owner_id_seq; Type: SEQUENCE SET; Schema: public; Owner: doadmin
--

SELECT pg_catalog.setval('public.owner_owner_id_seq', 24, true);


--
-- Name: vaccinations_vaccine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: doadmin
--

SELECT pg_catalog.setval('public.vaccinations_vaccine_id_seq', 18, true);


--
-- Name: vet_vet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: doadmin
--

SELECT pg_catalog.setval('public.vet_vet_id_seq', 13, true);


--
-- Name: animal animal_pkey; Type: CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.animal
    ADD CONSTRAINT animal_pkey PRIMARY KEY (animal_id);


--
-- Name: history_bird history_bird_pkey; Type: CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_bird
    ADD CONSTRAINT history_bird_pkey PRIMARY KEY (case_id, animal_id);


--
-- Name: history_cat history_cat_pkey; Type: CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_cat
    ADD CONSTRAINT history_cat_pkey PRIMARY KEY (case_id, animal_id);


--
-- Name: history_dog history_dog_pkey; Type: CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_dog
    ADD CONSTRAINT history_dog_pkey PRIMARY KEY (case_id, animal_id);


--
-- Name: history_reptile history_reptile_pkey; Type: CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_reptile
    ADD CONSTRAINT history_reptile_pkey PRIMARY KEY (case_id, animal_id);


--
-- Name: medical medical_pkey; Type: CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.medical
    ADD CONSTRAINT medical_pkey PRIMARY KEY (medical_id);


--
-- Name: medicine medicine_pkey; Type: CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.medicine
    ADD CONSTRAINT medicine_pkey PRIMARY KEY (medicine_id);


--
-- Name: owner owner_pkey; Type: CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.owner
    ADD CONSTRAINT owner_pkey PRIMARY KEY (owner_id);


--
-- Name: vaccinations vaccinations_pkey; Type: CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.vaccinations
    ADD CONSTRAINT vaccinations_pkey PRIMARY KEY (vaccine_id);


--
-- Name: vet vet_pkey; Type: CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.vet
    ADD CONSTRAINT vet_pkey PRIMARY KEY (vet_id);


--
-- Name: vet vet_username_key; Type: CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.vet
    ADD CONSTRAINT vet_username_key UNIQUE (username);


--
-- Name: animal animal_owner_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.animal
    ADD CONSTRAINT animal_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES public.owner(owner_id);


--
-- Name: animal animal_vet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.animal
    ADD CONSTRAINT animal_vet_id_fkey FOREIGN KEY (vet_id) REFERENCES public.vet(vet_id);


--
-- Name: history_bird history_bird_animal_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_bird
    ADD CONSTRAINT history_bird_animal_id_fkey FOREIGN KEY (animal_id) REFERENCES public.animal(animal_id);


--
-- Name: history_bird history_bird_vet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_bird
    ADD CONSTRAINT history_bird_vet_id_fkey FOREIGN KEY (vet_id) REFERENCES public.vet(vet_id);


--
-- Name: history_cat history_cat_animal_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_cat
    ADD CONSTRAINT history_cat_animal_id_fkey FOREIGN KEY (animal_id) REFERENCES public.animal(animal_id);


--
-- Name: history_cat history_cat_vet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_cat
    ADD CONSTRAINT history_cat_vet_id_fkey FOREIGN KEY (vet_id) REFERENCES public.vet(vet_id);


--
-- Name: history_dog history_dog_animal_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_dog
    ADD CONSTRAINT history_dog_animal_id_fkey FOREIGN KEY (animal_id) REFERENCES public.animal(animal_id);


--
-- Name: history_dog history_dog_vet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_dog
    ADD CONSTRAINT history_dog_vet_id_fkey FOREIGN KEY (vet_id) REFERENCES public.vet(vet_id);


--
-- Name: history_reptile history_reptile_animal_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_reptile
    ADD CONSTRAINT history_reptile_animal_id_fkey FOREIGN KEY (animal_id) REFERENCES public.animal(animal_id);


--
-- Name: history_reptile history_reptile_vet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.history_reptile
    ADD CONSTRAINT history_reptile_vet_id_fkey FOREIGN KEY (vet_id) REFERENCES public.vet(vet_id);


--
-- Name: medical medical_animal_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.medical
    ADD CONSTRAINT medical_animal_id_fkey FOREIGN KEY (animal_id) REFERENCES public.animal(animal_id);


--
-- Name: medicine medicine_animal_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.medicine
    ADD CONSTRAINT medicine_animal_id_fkey FOREIGN KEY (animal_id) REFERENCES public.animal(animal_id);


--
-- Name: medicine medicine_medical_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.medicine
    ADD CONSTRAINT medicine_medical_id_fkey FOREIGN KEY (medical_id) REFERENCES public.medical(medical_id);


--
-- Name: vaccinations vaccinations_animal_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: doadmin
--

ALTER TABLE ONLY public.vaccinations
    ADD CONSTRAINT vaccinations_animal_id_fkey FOREIGN KEY (animal_id) REFERENCES public.animal(animal_id);


--
-- PostgreSQL database dump complete
--

