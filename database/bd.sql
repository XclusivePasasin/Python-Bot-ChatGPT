-- Create database
CREATE DATABASE Online_Shop;

-- Use the created database
USE Online_shop;

-- Create table Products
CREATE TABLE Products (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Primary key for the product',
    name VARCHAR(255) NOT NULL COMMENT 'Name of the product',
    price DECIMAL(10, 2) NOT NULL COMMENT 'Price of the product',
    description TEXT NOT NULL COMMENT 'Description of the product',
    availability VARCHAR(1) NOT NULL COMMENT 'Availability status: E (Exhausted), A (Available)'
);

INSERT INTO Products (name, price, description, availability) VALUES
('Lipstick', ROUND(RAND() * (50 - 10) + 10, 2), 'Long-lasting vibrant color lipstick.', 'A'),
('Moisturizer', ROUND(RAND() * (100 - 20) + 20, 2), 'Hydrating facial moisturizer.', 'A'),
('Shampoo', ROUND(RAND() * (30 - 5) + 5, 2), 'Nourishing shampoo for all hair types.', 'A'),
('Conditioner', ROUND(RAND() * (30 - 5) + 5, 2), 'Smoothing conditioner with natural ingredients.', 'E'),
('Facial Cleanser', ROUND(RAND() * (50 - 15) + 15, 2), 'Gentle facial cleanser for daily use.', 'A'),
('Sunscreen', ROUND(RAND() * (40 - 15) + 15, 2), 'Broad spectrum SPF 50 sunscreen.', 'A'),
('Foundation', ROUND(RAND() * (60 - 20) + 20, 2), 'Full coverage liquid foundation.', 'E'),
('Eye Cream', ROUND(RAND() * (80 - 25) + 25, 2), 'Anti-aging eye cream.', 'A'),
('Perfume', ROUND(RAND() * (150 - 50) + 50, 2), 'Luxury fragrance for special occasions.', 'A'),
('Body Lotion', ROUND(RAND() * (45 - 10) + 10, 2), 'Moisturizing body lotion for soft skin.', 'A'),
('THE ORDINARY Natural Moisturizing Factors + HA 30ML', 17.99, 'Una crema hidratante facial con Ácido Hialurónico enfocada a potenciar los factores de hidratación naturales de la dermis', 'A'),
('ISDIN Acniben Control De Brillo Y Granos 40ml', 28.99, 'Crema facial para el control de brillos y granos De textura ligera y no grasa, Acniben Control brillos y granos es un gel', 'A'),
('NEUTROGENA Oil Free Acne Mositurizer', 17.99, 'Humectante liviano y sin aceite para uso diario combate los brotes e hidrata al mismo tiempo, para una piel suave y libre', 'A'),
('NEUTROGENA Hidro Boost Water Gel 48gr', 27.99, 'Hidrata la piel seca al instante y le deja un brillo de aspecto saludable todos los días. Esta fórmula premiada con ácido', 'A'),
('AVENE Ultra Mat Fuide 50ml', 28.99, 'Ultra Mat Fluido SPF 50+, es un protector solar para piel sensible. Resistente al agua con protección de amplio espectro', 'A'),
('EUCERIN Sun Gel-Crema Oil Control 50ml', 28.99, 'EUCERIN Sun Gel-Crema Oil Control Toque Seco FPS 50 Protección solar facial para piel grasa y propensa al acné, con accion', 'A'),
('VICHY Capital Soleil Matificante 3 En 1 50ml', 31.99, 'VICHY Capital Soleil Matificante 3 en 1 Vichy Capital Soleil es un protector solar SPF50+ de uso diario para pieles mixtas', 'A'),
('ISDIN Fusion Water Magic 50ml', 33.50, 'Fusion Water MAGIC SPF 50 Fotoprotector facial de textura ultraligera y fase externa acuosa con acabado final sedoso Protege', 'A'),
('THE ORDINARY Ácido Hialurónico 30ml', 18.50, 'THE ORDINARY Ácido hialurónico 2 % + B5 Sérum hidratante Ácido hialurónico 2 % + B5 Sérum hidratante. Un sérum hidratante', 'A'),
('THE ORDINARY Salicylic Acid 30ml', 16.99, 'THE ORDINARY Salicylic Acid 2% Solution Tratamiento Ácido Salicílico El ácido salicílico es un tratamiento exfoliante para', 'A'),
('THE ORDINARY Lactic Acid 10% + HA 30ml', 18.99, 'THE ORDINARY Lactic Acid 10% + HA | Sérum Exfoliante The Ordinary El sérum exfoliante es un exfoliante suavea base de ácido', 'A'),
('THE ORDINARY AHA 30% + BHA 30ml', 19.50, 'THE ORDINARY AHA 30% + BHA 2% Peeling SolutionAHA 30% + BHA 2% Peeling Solution AHA 30% + BHA 2% Peeling Solution es una', 'A'),
('AVENE Cleanance Comedomed Anti Imperfecciones 30ml', 26.99, 'Piel mixta a grasa y/o con tendencia acnéica Cuidado único que reduce las imperfecciones visibles y previene su reaparición', 'A'),
('OLAPLEX Kit Strong Days', 79.95, 'Experimente la magia de los productos más vendidos de OLAPLEX con esta sencilla rutina de cuidado del cabello para lograr', 'A'),
('COLOR WOW Dream Coat Anti Frizz', 44.95, 'Dream Coat, con tecnología anti-frizz y anti-humedad. Este tratamiento superligero sin aclarado hace que el cabello sea', 'A'),
('EUCERIN Anti-Pigment Corrector De Manchas 50ml', 26.99, 'Eucerin Anti-Pigment Corrector de manchas es un gel no graso con un aplicador de uso tópico que facilita la aplicación precisa', 'A'),
('AVENE Cleanance Gel Limpiador 200ml', 25.99, 'Un gel limpiador purificante con una espuma ligera para pieles grasas y/o con tendencia acneica. Su fórmula respetuosa con', 'A'),
('CERAVE Foaming Cleanser 8 Fl Oz', 25.99, 'Limpiador facial de espuma CeraVe tiene una fórmula única con tres ceramidas esenciales (1, 3, 6-II) que limpia y elimina', 'A'),
('Cerave Foaming Cleanser Barra', 16.99, 'Limpiador facial en barra CeraVe tiene una fórmula única con tres ceramidas esenciales (1, 3, 6-II) que limpia y elimina', 'A'),
('ISDIN Acniben Limpiador Purificante 150ml', 25.99, 'Acniben Limpiador purificante Elimina el exceso de grasa y puriﬁca la piel de forma suave Acniben Limpiador Purificante', 'A'),
('RUTINA PIEL MIXTA A GRASA', 82.99, 'Rutina Eucerin para una Piel Mate, Hidratada y Protegida ENVIO GRATIS A DOMICILIO', 'A'),
('DUO HIDRATANTE PIELES SECAS', 74.99, 'Dúo Hidratante para una Piel Suave y Nutrida Paso 1 - Hidratación Profunda: Serum Hyalu B5 de La Roche-Posay Aplica el Serum', 'A'),
('Pack Neutrogena Hydro Boost Gel De Agua 50 Ml + Contorno De Ojos 15 Ml', 39.99, 'BENEFICIOS NEUTROGENA HYDRO BOOST GEL DE AGUA: es una hidratante que combina una textura ligera con una hidratación continua', 'A'),
('MISSHA Essence Sun SPF45 50ml', 21.95, 'Protector solar químico viene en una fórmula liviana y no pegajosa que se siente refrescante en la piel. Contiene extractos', 'A'),
('MISSHA Softh Finish Sun Milk SPF50+', 23.95, 'Protector solar que brinda una protección SPF50+ PA+++ para bloquear efectivamente los rayos UVA y UVB. Su fórmula, ligera', 'A'),
('ETUDE My Lash Serum 9 Gr', 11.95, 'My Lash Serum Alarga Pestañas Etude House, se trata de un serum para pestañas que promete un aspecto más saludable, y con', 'A'),
('MARY&MAY - Crema Contorno De Ojos 12gr', 11.99, 'Crema contorno de ojos enriquecida con 1.000 ppm de ácido tranexámico y glutatión para eliminar las ojeras y revitalizar', 'A');

