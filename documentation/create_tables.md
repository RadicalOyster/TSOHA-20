**Create Table**

```sqlite3
CREATE TABLE account (
        id INTEGER NOT NULL,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (username)
)

CREATE TABLE role (
        id INTEGER NOT NULL,
        name VARCHAR(40) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (name)
)

CREATE TABLE creature (
        id INTEGER NOT NULL,
        name VARCHAR(100) NOT NULL,
        hp INTEGER NOT NULL,
        formula VARCHAR(40),
        ac INTEGER NOT NULL,
        speed INTEGER NOT NULL,
        swimspeed INTEGER,
        flyspeed INTEGER,
        cr VARCHAR(20),
        str INTEGER NOT NULL,
        dex INTEGER NOT NULL,
        con INTEGER NOT NULL,
        int INTEGER NOT NULL,
        wis INTEGER NOT NULL,
        cha INTEGER NOT NULL,
        proficiency INTEGER NOT NULL,
        strsav BOOLEAN NOT NULL,
        dexsav BOOLEAN NOT NULL,
        consav BOOLEAN NOT NULL,
        intsav BOOLEAN NOT NULL,
        wissav BOOLEAN NOT NULL,
        chasav BOOLEAN NOT NULL,
        athletics BOOLEAN NOT NULL,
        acrobatics BOOLEAN NOT NULL,
        soh BOOLEAN NOT NULL,
        stealth BOOLEAN NOT NULL,
        arcana BOOLEAN NOT NULL,
        history BOOLEAN NOT NULL,
        investigation BOOLEAN NOT NULL,
        nature BOOLEAN NOT NULL,
        religion BOOLEAN NOT NULL,
        animal BOOLEAN NOT NULL,
        insight BOOLEAN NOT NULL,
        medicine BOOLEAN NOT NULL,
        perception BOOLEAN NOT NULL,
        survival BOOLEAN NOT NULL,
        deception BOOLEAN NOT NULL,
        intimidation BOOLEAN NOT NULL,
        performance BOOLEAN NOT NULL,
        persuasion BOOLEAN NOT NULL,
        PRIMARY KEY (id),
        CHECK (strsav IN (0, 1)),
        CHECK (dexsav IN (0, 1)),
        CHECK (consav IN (0, 1)),
        CHECK (intsav IN (0, 1)),
        CHECK (wissav IN (0, 1)),
        CHECK (chasav IN (0, 1)),
        CHECK (athletics IN (0, 1)),
        CHECK (acrobatics IN (0, 1)),
        CHECK (soh IN (0, 1)),
        CHECK (stealth IN (0, 1)),
        CHECK (arcana IN (0, 1)),
        CHECK (history IN (0, 1)),
        CHECK (investigation IN (0, 1)),
        CHECK (nature IN (0, 1)),
        CHECK (religion IN (0, 1)),
        CHECK (animal IN (0, 1)),
        CHECK (insight IN (0, 1)),
        CHECK (medicine IN (0, 1)),
        CHECK (perception IN (0, 1)),
        CHECK (survival IN (0, 1)),
        CHECK (deception IN (0, 1)),
        CHECK (intimidation IN (0, 1)),
        CHECK (performance IN (0, 1)),
        CHECK (persuasion IN (0, 1))
)

CREATE TABLE ability (
        id INTEGER NOT NULL,
        name VARCHAR(100) NOT NULL,
        description VARCHAR(10000) NOT NULL,
        "toHit" INTEGER NOT NULL,
        PRIMARY KEY (id)
)

CREATE TABLE damage_type (
        id INTEGER NOT NULL,
        type VARCHAR(40) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (type)
)

CREATE TABLE account_role (
        id INTEGER NOT NULL,
        role_id INTEGER,
        user_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(role_id) REFERENCES role (id),
        FOREIGN KEY(user_id) REFERENCES account (id)
)

CREATE TABLE account_creature (
        id INTEGER NOT NULL,
        creature_id INTEGER,
        user_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(creature_id) REFERENCES creature (id),
        FOREIGN KEY(user_id) REFERENCES account (id)
)

CREATE TABLE "Creature_Ability" (
        id INTEGER NOT NULL,
        creature_id INTEGER,
        ability_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(creature_id) REFERENCES creature (id),
        FOREIGN KEY(ability_id) REFERENCES ability (id)
)

CREATE TABLE attack (
        id INTEGER NOT NULL,
        ability_id INTEGER,
        "damageFormula" VARCHAR(40) NOT NULL,
        damagetype_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(ability_id) REFERENCES ability (id),
        FOREIGN KEY(damagetype_id) REFERENCES damage_type (id)
)
```