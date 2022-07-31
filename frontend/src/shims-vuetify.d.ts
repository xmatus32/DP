declare module "vuetify";
declare module "vuetify/lib/components";
declare module "vuetify/lib/directives";
declare module "*.vue" {
  import { defineComponent } from "vue";
  const component: ReturnType<typeof defineComponent>;
  export default component;
}
