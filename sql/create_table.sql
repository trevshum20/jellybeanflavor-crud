-- Table: public.jellybeans_jellybeanflavor

-- DROP TABLE IF EXISTS public.jellybeans_jellybeanflavor;

CREATE TABLE IF NOT EXISTS public.jellybeans_jellybeanflavor
(
    id bigint NOT NULL DEFAULT nextval('jellybeans_jellybeanflavor_id_seq'::regclass),
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    description character varying(255) COLLATE pg_catalog."default" NOT NULL,
    "photoUrl" character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT jellybeans_jellybeanflavor_pkey PRIMARY KEY (id),
    CONSTRAINT jellybeans_jellybeanflavor_name_key UNIQUE (name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.jellybeans_jellybeanflavor
    OWNER to postgres;
-- Index: jellybeans_jellybeanflavor_name_27cfb070_like

-- DROP INDEX IF EXISTS public.jellybeans_jellybeanflavor_name_27cfb070_like;

CREATE INDEX IF NOT EXISTS jellybeans_jellybeanflavor_name_27cfb070_like
    ON public.jellybeans_jellybeanflavor USING btree
    (name COLLATE pg_catalog."default" varchar_pattern_ops ASC NULLS LAST)
    TABLESPACE pg_default;